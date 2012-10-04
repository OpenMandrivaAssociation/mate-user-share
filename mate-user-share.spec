%define materel 1.4
%define uprel 1

Summary: MATE user file sharing
Name: mate-user-share
Version: %{materel}.%{uprel}
Release: 1
License: GPLv2+
Group: System/Servers
URL: http://www.mate-desktop.org
Source0: http://pub.mate-desktop.org/releases/%{materel}/mate-user-share-%{version}.tar.xz
Suggests: apache
Suggests: apache-mod_dnssd >= 0.6
Requires: obex-data-server >= 0.3
BuildRequires: apache-mod_dnssd
BuildRequires: mate-common
BuildRequires: mate-conf-devel
BuildRequires: pkgconfig(libmatenotify)
BuildRequires: mate-bluetooth-devel
BuildRequires: dbus-glib-devel
BuildRequires: pkgconfig(libcanberra-gtk)
BuildRequires: unique-devel
BuildRequires: pkgconfig(libcaja-extension)
BuildRequires: intltool
BuildRequires: mate-doc-utils
BuildRequires:	desktop-file-utils

%description
This program enables user to share directories through Webdav or Bluetooth
(over ObexFTP).

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--with-modules-path=%_sysconfdir/httpd/modules \
	--disable-schemas-install
%make

%install
%makeinstall_std
desktop-file-edit --remove-category=MATE --add-category=X-MATE %{buildroot}%{_datadir}/applications/mate-user-share-properties.desktop
%find_lang %name --with-gnome

%files -f %name.lang
%doc README ChangeLog NEWS
%_sysconfdir/xdg/autostart/mate-user-share.desktop
%{_sysconfdir}/mateconf/schemas/desktop_mate_file_sharing.schemas
%{_bindir}/*
%{_datadir}/mate-user-share
%_datadir/applications/mate-user-share-properties.desktop
%_libexecdir/mate-user-share
%_datadir/icons/hicolor/*/apps/*.*
%_libdir/caja/extensions-2.0/libcaja-share-extension.so
