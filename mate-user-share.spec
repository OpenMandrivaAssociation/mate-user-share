%define url_ver %(echo %{version}|cut -d. -f1,2)

Name:           mate-user-share
Version:        1.6.0
Release:        1
License:        GPLv2+
Summary:        MATE  user file sharing
URL:            http://mate-desktop.org
Group:          System/Servers
Source0:        http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
# This patch fixes 'AM_CONFIG_HEADER' macro is deprecated error
Patch0:         mate-user-share-1.6.0-mga-fix-configure_in-script.patch

BuildRequires:  apache-devel
BuildRequires:  itstool
BuildRequires:  libxml2-utils
BuildRequires:  intltool
BuildRequires:  xml2po
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  hicolor-icon-theme
BuildRequires:  mate-common
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libcaja-extension)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libcanberra-gtk)
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(mate-bluetooth-1.0)
BuildRequires:  pkgconfig(mate-doc-utils)
BuildRequires:  pkgconfig(unique-1.0)

Suggests:       apache
Suggests:       apache-mod_dnssd >= 0.6
Requires:       obex-data-server >= 0.3

%description
This program enables user to share directories through Webdav or Bluetooth
(over ObexFTP).

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
   --disable-schemas-install \
   --with-modules-path=%{_sysconfdir}/httpd/modules \
   --disable-scrollkeeper
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README COPYING
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/mate-file-share-properties
%{_libexecdir}/%{name}/
%{_libdir}/caja/
%{_datadir}/%{name}/
%{_datadir}/applications/mate-user-share-properties.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/glib-2.0/schemas/org.mate.FileSharing.gschema.xml
%{_datadir}/MateConf/*


