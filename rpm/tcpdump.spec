Summary: A network traffic monitoring tool
Name: tcpdump
Version: 4.99.3
Release: 1
License: BSD with advertising
URL: https://github.com/sailfishos/tcpdump
Requires(pre): shadow-utils
BuildRequires: openssl-devel
BuildRequires: libpcap-devel
BuildRequires: automake
BuildRequires: sharutils

Source0: %{name}-%{version}.tar.gz

%description
Tcpdump is a command-line tool for monitoring network traffic.
Tcpdump can capture and display the packet headers on a particular
network interface or on all interfaces.  Tcpdump can display all of
the packet headers, or just the ones that match particular criteria.

Install tcpdump if you need a program to monitor network traffic.

%prep
%autosetup -n %{name}-%{version}/%{name}

find . -name '*.c' -o -name '*.h' | xargs chmod 644

%build
export CFLAGS="$RPM_OPT_FLAGS $(getconf LFS_CFLAGS) -fno-strict-aliasing"

%configure --with-crypto --with-user=tcpdump --without-smi
%make_build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}

install -m755 tcpdump ${RPM_BUILD_ROOT}%{_sbindir}

%pre
/usr/sbin/groupadd -g 72 tcpdump 2> /dev/null
/usr/sbin/useradd -u 72 -g 72 -s /sbin/nologin -M -r \
	-d / tcpdump 2> /dev/null
exit 0

%files
%defattr(-,root,root)
%license LICENSE
%{_sbindir}/tcpdump
