%include	/usr/lib/rpm/macros.perl
%define		__find_requires %{_builddir}/Parse-RecDescent-%{version}/find-perl-requires
Summary:	Perl Parse::RecDescent module
Summary(pl):	Modu³ Perla Parse::RecDescent
Name:		perl-Parse-RecDescent
Version:	1.77
Release:	2
License:	Perl Artistic License
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Parse/Parse-RecDescent-%{version}.tar.gz
Patch0:		perl-Parse-RecDescent-paths.patch
Patch1:		perl-Parse-RecDescent-dep.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
Requires:	perl
Requires:	%{perl_sitearch}
Obsoletes:	perl-Text-Balanced
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl Parse::RecDescent module.

%description -l pl
Modu³ Perla Parse::RecDescent.

%prep
%setup -q -n Parse-RecDescent-%{version}
%patch0 -p1
%patch1 -p1

chmod +x find-perl-requires

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Parse/RecDescent
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Changes}.gz
%{perl_sitelib}/Parse/*
%{perl_sitelib}/Text/*

%dir %{perl_sitearch}/auto/Parse/RecDescent
%{perl_sitearch}/auto/Parse/RecDescent/.packlist

%{_mandir}/man3/*
