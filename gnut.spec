Summary:	Gnutella, a file sharing tool
Summary(pl.UTF-8):	Gnutella - narzędzie do wymiany plików
Name:		gnut
Version:	0.4.28
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://www.gnutelliums.com/linux_unix/gnut/tars/%{name}-%{version}.tar.gz
# Source0-md5:	bade24c9838d390de41f5ea0c80dc22f
URL:		http://www.gnutelliums.com/linux_unix/gnut/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnutella is a simple ncurses client for Gnutella file-sharing
protocol.

%description -l pl.UTF-8
Gnutella jest prostym klientem protokołu wymiany plików Gnutella,
działającym w środowiskach ncurses.

%prep
%setup -q

%build
rm -f missing
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--disable-gtktest <<END


END

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog doc/TUTORIAL doc/*.html
%attr(755,root,root) %{_bindir}/gnut
