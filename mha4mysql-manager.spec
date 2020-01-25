Summary:	Master High Availability Manager and Tools for MySQL, Manager Package
Name:		mha4mysql-manager
Version:	0.54
Release:	1
License:	GPL v2
Group:		Applications/Databases
URL:		http://code.google.com/p/mysql-master-ha/
Source0:	https://mysql-master-ha.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	3072bf53788f867026e2e6eec0e77644
BuildRequires:	mha4mysql-node >= 0.54
BuildRequires:	perl-Config-Tiny
BuildRequires:	perl-DBD-mysql
BuildRequires:	perl-DBI
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-Log-Dispatch
BuildRequires:	perl-Parallel-ForkManager
BuildRequires:	perl-Time-HiRes
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	mha4mysql-node >= 0.54
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Master High Availability Manager and tools for MySQL (MHA) for
automating master failover and fast master switch.

This package contains manager scripts.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/mha4mysql/manager/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/masterha_check_repl
%attr(755,root,root) %{_bindir}/masterha_check_ssh
%attr(755,root,root) %{_bindir}/masterha_check_status
%attr(755,root,root) %{_bindir}/masterha_conf_host
%attr(755,root,root) %{_bindir}/masterha_manager
%attr(755,root,root) %{_bindir}/masterha_master_monitor
%attr(755,root,root) %{_bindir}/masterha_master_switch
%attr(755,root,root) %{_bindir}/masterha_secondary_check
%attr(755,root,root) %{_bindir}/masterha_stop
%{_mandir}/man1/masterha_check_repl.1p*
%{_mandir}/man1/masterha_check_ssh.1p*
%{_mandir}/man1/masterha_check_status.1p*
%{_mandir}/man1/masterha_conf_host.1p*
%{_mandir}/man1/masterha_manager.1p*
%{_mandir}/man1/masterha_master_monitor.1p*
%{_mandir}/man1/masterha_master_switch.1p*
%{_mandir}/man1/masterha_secondary_check.1p*
%{_mandir}/man1/masterha_stop.1p*
%{perl_vendorlib}/MHA/*.pm
