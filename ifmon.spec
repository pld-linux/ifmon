Summary:	IFMon - interface monitor
Summary(pl.UTF-8):	IFMon - monitor interfejsów
Name:		ifmon
Version:	2.2.1
Release:	1
License:	GPL-like
Group:		X11/Applications/Graphics
Source0:	http://wolfsinger.com/~wolfpack/packages/%{name}-%{version}.tar.bz2
# Source0-md5:	01ddd0a36dbbbe778a69d0fbf1763f12
Patch0:		%{name}-verbose.patch
URL:		http://freecode.com/projects/interface-monitor
BuildRequires:	gtk+-devel >= 1.2.10
BuildRequires:	libstdc++-devel
Requires:	gtk+ >= 1.2.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IFMon (Interface Monitor) displays the traffic, state, connection, and
other information of a network interface as a small console window.
The information for the network interface being monitored is obtained
from the files in /proc to help simplify portability.

%description -l pl.UTF-8
IFMon (Interface Monitor) wyświetla informacje o ruchu, stanie,
połączeniach oraz inne dotyczące interfejsu sieciowego w małym oknie
konsoli. Informacje dotyczące monitorowanego interfejsu są pobierane z
plików w /proc, co ma na celu ułatwienie przenośności.

%prep
%setup -q
%patch0 -p1

%build
./configure Linux
%{__make} \
	CC="%{__cc}" \
	CPP="%{__cc} %{rpmldflags}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -DPREFIX=\\\"%{_prefix}\\\" `gtk-config --cflags`" \
	LIB_DIRS=

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	INSTBINFLAGS="-m755"

bzip2 -d $RPM_BUILD_ROOT%{_mandir}/man1/*.bz2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/ifmon
%{_mandir}/man1/ifmon.1*
