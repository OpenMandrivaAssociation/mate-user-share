%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE user file sharing
Name:		mate-user-share
Version:	1.26.0
Release:	2
License:	GPLv2+
Group:		System/Servers
Url:		https://www.mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	autoconf-archive
BuildRequires:	apache-devel
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gdk-x11-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(unique-3.0)
BuildRequires:	yelp-tools

Recommends:	apache-mod_dav >= 2.2
Recommends:	apache-mod_dnssd >= 0.6
Recommends:	obex-data-server >= 0.3

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides a small applicatoin that binds together various free
software projects to bring easy to use user-level file sharing to the
masses.

The program is meant to run in the background when the user is logged
in, and when file sharing is enabled a webdav server is started that
shares the $HOME/Public folder. The share is then published to all
computers on the local network using mDNS/rendezvous, so that it shows
up in the Network location in MATE.

The dav server used is apache, so you need that installed. Avahi or 
Howl is used for mDNS support, so you need to have that installed and
mDNSResolver running.

%files -f %{name}.lang
%doc README ChangeLog NEWS COPYING
%{_sysconfdir}/xdg/autostart/%{name}-obexftp.desktop
%{_sysconfdir}/xdg/autostart/%{name}-obexpush.desktop
%{_sysconfdir}/xdg/autostart/%{name}-webdav.desktop
%{_libexecdir}/%{name}
%{_bindir}/*
%{_datadir}/applications/mate-user-share-properties.desktop
%{_datadir}/glib-2.0/schemas/org.mate.FileSharing.gschema.xml
%{_datadir}/mate-user-share
%{_iconsdir}/hicolor/*/apps/*.*
%{_mandir}/man1/mate-file-share-properties.1*
%{_libdir}/caja/extensions-2.0/libcaja-user-share.so
%{_datadir}/caja/extensions/libcaja-user-share.caja-extension

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%configure \
	--disable-schemas-compile \
	--with-modules-path=%{_sysconfdir}/httpd/modules \
	%{nil}
%make_build

%install
%make_install

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-obexftp.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-obexpush.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-webdav.desktop

