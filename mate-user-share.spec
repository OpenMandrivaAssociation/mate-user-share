%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE user file sharing
Name:		mate-user-share
Version:	1.18.0
Release:	1
License:	GPLv2+
Group:		System/Servers
Url:		http://www.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(unique-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
Suggests:	apache
Suggests:	apache-mod_dnssd >= 0.6
Requires:	obex-data-server >= 0.3

%description
This program enables user to share directories through Webdav or Bluetooth
(over ObexFTP).

%prep
%setup -q

%build
%configure \
	--with-modules-path=%{_sysconfdir}/httpd/modules \
	%{nil}
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README ChangeLog NEWS COPYING
%{_sysconfdir}/xdg/autostart/mate-user-share-obexftp.desktop
%{_sysconfdir}/xdg/autostart/mate-user-share-obexpush.desktop
%{_sysconfdir}/xdg/autostart/mate-user-share-webdav.desktop
%{_bindir}/*
%{_datadir}/applications/mate-user-share-properties.desktop
%{_datadir}/glib-2.0/schemas/org.mate.FileSharing.gschema.xml
%{_datadir}/mate-user-share
%{_iconsdir}/hicolor/*/apps/*.*
%{_libdir}/caja/extensions-2.0/libcaja-user-share.so
%{_datadir}/caja/extensions/libcaja-user-share.caja-extension
%{_libexecdir}/mate-user-share
%{_mandir}/man1/mate-file-share-properties.1*

