%include	/usr/lib/rpm/macros.perl
%define		__find_requires %{_builddir}/Parse-RecDescent-%{version}/find-perl-requires
Summary:	Perl Parse::RecDescent module
Summary(pl):	Modu� Perla Parse::RecDescent
Name:		perl-Parse-RecDescent
Version:	1.79
Release:	2
License:	Perl Artistic License
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Parse/Parse-RecDescent-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-dep.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
Requires:	perl
Requires:	%{perl_sitearch}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-Text-Balanced

%description
Perl Parse::RecDescent module.

%description -l pl
Modu� Perla Parse::RecDescent.

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

gzip -9nf README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Parse/*
%{perl_sitelib}/Text/*
%{_mandir}/man3/*
