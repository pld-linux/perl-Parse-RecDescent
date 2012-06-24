#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Parse
%define		pnam	RecDescent
Summary:	Parse::RecDescent - generate recursive-descent parsers
Summary(pl):	Parse::RecDescent - generowanie zmniejszaj�cych rekurencyjnie analizator�w
Name:		perl-Parse-RecDescent
Version:	1.94
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	497600b337a501eae11f31195ccec9d4
Patch0:		%{name}-paths.patch
BuildRequires:	perl-Text-Balanced
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
# these versions included own copy of Text::Balanced
BuildConflicts:	perl-Parse-RecDescent < 1.92
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Calc)'

%description
RecDescent incrementally generates top-down recursive-descent text
parsers from simple yacc-like grammar specifications. It provides:
 * Regular expressions or literal strings as terminals (tokens),
 * Multiple (non-contiguous) productions for any rule,
 * Repeated, optional and alternate subrules within productions,
 * Late-bound (run-time dispatched) subrules,
 * Full access to Perl within actions specified as part of the
   grammar,
 * Simple automated error reporting during parser generation and
   parsing,
 * The ability to commit to, uncommit to, or reject particular
   productions during a parse,
 * Incremental extension of the parsing grammar (even during a
   parse),
 * Precompilation of parser objects,
 * User-definable reduce-reduce conflict resolution via
   "scoring" of matching productions.

%description -l pl
RecDescent generuje przyrostowo zst�puj�ce, zmniejszaj�ce
rekurencyjnie analizatory tekstu w oparciu o prost� specyfikacj�
gramatyki, podobn� do u�ywanej przez yacca. Udost�pnia on:
 * Wyra�enia regularne i �a�cuchy litera��w jako terminale (tokeny),
 * Wielokrotn� (nieci�g��) produkcj� dla ka�dej regu�y,
 * Powtarzane, opcjonalne i alternatywne podregu�y w obr�bie
   produkcji,
 * Podregu�y p�nego wi�zania (wysy�ane w chwili uruchomienia),
 * Pe�en dost�p do Perla w obr�bie akcji okre�lonych jako cz��
   gramatyki,
 * Proste, zautomatyzowane sygnalizowanie b��d�w podczas generacji
   analizatora i podczas analizy,
 * Mo�liwo�� zatwierdzenia, cofni�cia oraz odrzucania poszczeg�lnych
   produkcji podczas analizy,
 * Przyrostowe rozszerzanie gramatyki podlegaj�cej analizie (nawet
   podczas samej analizy),
 * Prekompilacj� obiekt�w analizatora,
 * Definiowalne przez u�ytkownika rozpoznawanie konflikt�w
   "reduce-reduce" poprzez ocenianie dopasowania produkcji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/Parse/*.pm
%{_mandir}/man3/*
