Summary:	Gnutella, a file sharing tool
Summary(pl):	Gnutella - narzêdzie do wymiany plików
Name:		gnut
Version:	0.4.28
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://www.gnutelliums.com/linux_unix/gnut/tars/%{name}-%{version}.tar.gz
URL:		http://www.gnutelliums.com/linux_unix/gnut/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnutella is a simple ncurses client for Gnutella file-sharing
protocol.

%description -l pl
Gnutella jest prostym klientem protoko³u wymiany plików Gnutella,
dzia³aj±cym w ¶rodowiskach ncurses.

%prep
%setup -q

%build
aclocal -I macros
autoconf
rm -f missing
automake -a -c
%configure \
	--disable-gtktest <<END


END

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS ChangeLog doc/TUTORIAL doc/*.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/gnut
