%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Perl Parse::RecDescent module
Summary(pl):	Modu³ Perla Parse::RecDescent
Name:		perl-Parse-RecDescent
Version:	1.66
Release:	1
Copyright:	Perl Artistic License
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Parse-RecDescent-%{version}.tar.gz
Patch:		perl-Parse-RecDescent.patch
BuildRequires:	perl >= 5.005_03-10
Requires:	perl
Requires:	%{perl_sitelib}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Perl Parse::RecDescent module.

%description -l pl
Modu³ Perla Parse::RecDescent.

%prep
%setup -q -n Parse-RecDescent-%{version}
%patch -p1

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_archlib}

make install \
	DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Parse/RecDescent
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Parse
%{perl_sitelib}/Text/*

%dir %{perl_sitearch}/auto/Parse/RecDescent

%{perl_sitearch}/auto/*/*/.packlist

%{_mandir}/man3/*
