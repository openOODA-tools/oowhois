Name:           oowhois
Version:        0.1.0
Release:        1%{?dist}
Summary:        Queries WHOIS and RDAP records for domain ownership, registrars, and CIDRs.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oowhois
Source0:        oowhois-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oowhois is a sovereign, capability-bounded DOMAIN REGISTRY written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oowhois
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oowhois-uninstall

%files
/usr/bin/oowhois
/usr/bin/oowhois-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
