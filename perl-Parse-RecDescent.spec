%include	/usr/lib/rpm/macros.perl
%define	pdir	Parse
%define	pnam	RecDescent
Summary:	Perl Parse::RecDescent module
Summary(pl):	Modu� Perla Parse::RecDescent
Name:		perl-Parse-RecDescent
Version:	1.80
Release:	6
License:	Perl Artistic License
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl-devel >= 5.6.1
Requires:	perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-Text-Balanced

%define		_noautoreq	"perl(Calc)"

%description
Perl Parse::RecDescent module.

%description -l pl
Modu� Perla Parse::RecDescent.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
