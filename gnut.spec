# $Revision: 1.7 $
Summary:	Gnutella, a file sharing tool
Name:		gnut
Version:	0.4.15
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://www.mrob.com/gnut/tars/%{name}-%{version}.tar.gz
URL:		http://www.mrob.com/gnut/
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnutella is a simple ncurses client for Gnutella file-sharing
protocol.

%description -l pl
Gnutella jest prostym klientem protokołu wymiany plików Gnutella,
działającym w środowiskach ncurses.

%prep
%setup -q

%build
%configure --disable-gtktest

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
