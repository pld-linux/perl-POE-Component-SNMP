#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%define		pdir	POE
%define		pnam	Component-SNMP
Summary:	POE::Component::SNMP - event-driven SNMP interface
Summary(pl.UTF-8):	POE::Component::SNMP - sterowany zdarzeniami interfejs do SNMP
Name:		perl-POE-Component-SNMP
Version:	1.1006
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9a2ef36ca0c40e030f0af35174a67172
URL:		http://search.cpan.org/dist/POE-Component-SNMP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-SNMP
BuildRequires:	perl-POE
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is an event-driven SNMP interface for POE.

%description -l pl.UTF-8
Ten moduł to sterowany zdarzeniami interfejs do SNMP dla POE.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"POE::Component::SNMP")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/SNMP.pm
%{perl_vendorlib}/POE/Component/SNMP
%{_mandir}/man3/*
