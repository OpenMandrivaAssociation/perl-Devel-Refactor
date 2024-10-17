%define upstream_name    Devel-Refactor
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	The *Devel::Refactor* module is for code refactoring
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

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

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 653409
- rebuild for updated spec-helper

* Sat Sep 26 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 449447
- import perl-Devel-Refactor


* Sat Sep 26 2009 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist
