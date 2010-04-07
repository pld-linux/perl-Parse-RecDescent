#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Parse
%define		pnam	RecDescent
Summary:	Parse::RecDescent - generate recursive-descent parsers
Summary(pl.UTF-8):	Parse::RecDescent - generowanie zmniejszających rekurencyjnie analizatorów
Name:		perl-Parse-RecDescent
Version:	1.965001
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DC/DCONWAY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e91351ad179a3843fbe8e521b135acaf
URL:		http://search.cpan.org/dist/Parse-RecDescent/
BuildRequires:	perl-Text-Balanced
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# these versions included own copy of Text::Balanced
BuildConflicts:	perl-Parse-RecDescent < 1.92
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Calc)'

%description
RecDescent incrementally generates top-down recursive-descent text
parsers from simple yacc-like grammar specifications. It provides:
- Regular expressions or literal strings as terminals (tokens),
- Multiple (non-contiguous) productions for any rule,
- Repeated, optional and alternate subrules within productions,
- Late-bound (run-time dispatched) subrules,
- Full access to Perl within actions specified as part of the grammar,
- Simple automated error reporting during parser generation and
  parsing,
- The ability to commit to, uncommit to, or reject particular
  productions during a parse,
- Incremental extension of the parsing grammar (even during a parse),
- Precompilation of parser objects,
- User-definable reduce-reduce conflict resolution via "scoring" of
  matching productions.

%description -l pl.UTF-8
RecDescent generuje przyrostowo zstępujące, zmniejszające
rekurencyjnie analizatory tekstu w oparciu o prostą specyfikację
gramatyki, podobną do używanej przez yacca. Udostępnia on:
- Wyrażenia regularne i łańcuchy literałów jako terminale (tokeny),
- Wielokrotną (nieciągłą) produkcję dla każdej reguły,
- Powtarzane, opcjonalne i alternatywne podreguły w obrębie produkcji,
- Podreguły późnego wiązania (wysyłane w chwili uruchomienia),
- Pełen dostęp do Perla w obrębie akcji określonych jako część
  gramatyki,
- Proste, zautomatyzowane sygnalizowanie błędów podczas generacji
  analizatora i podczas analizy,
- Możliwość zatwierdzenia, cofnięcia oraz odrzucania poszczególnych
  produkcji podczas analizy,
- Przyrostowe rozszerzanie gramatyki podlegającej analizie (nawet
  podczas samej analizy),
- Prekompilację obiektów analizatora,
- Definiowalne przez użytkownika rozpoznawanie konfliktów
  "reduce-reduce" poprzez ocenianie dopasowania produkcji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Parse/RecDescent/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/Parse/*.pm
%{_mandir}/man3/*
