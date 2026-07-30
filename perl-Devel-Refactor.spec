%define upstream_name    Devel-Refactor
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	The *Devel::Refactor* module is for code refactoring
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Devel-Refactor
Source0:	https://cpan.metacpan.org/authors/id/S/SS/SSOTKA/Devel-Refactor-0.05.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
The *Devel::Refactor* module is for code refactoring.

While *Devel::Refactor* may be used from Perl programs, it is also designed
to be used with the *EPIC* plug-in for the *eclipse* integrated development
environment.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

