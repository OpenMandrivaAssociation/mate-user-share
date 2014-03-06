%define url_ver %(echo %{version}|cut -d. -f1,2)

Name:           mate-user-share
Version:        1.8.0
Release:        1
License:        GPLv2+
Summary:        MATE  user file sharing
URL:            http://mate-desktop.org
Group:          System/Servers
Source0:        http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:  apache-devel
BuildRequires:  itstool
BuildRequires:  libxml2-utils
BuildRequires:  itstool
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  hicolor-icon-theme
BuildRequires:  mate-common
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libcaja-extension)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libcanberra-gtk)
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(unique-1.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  yelp-tools

Suggests:       apache

# already not working bluetooth support dropped by upstream:
Obsoletes:		mate-bluetooth
Obsoletes:		mate-file-manager-sendto-bluetooth
Obsoletes:		libmate-bluetooth-devel
Obsoletes:		libmate-bluetooth-gir1.0
Obsoletes:		libmate-bluetooth8
Conflicts:		mate-bluetooth
Conflicts:		mate-file-manager-sendto-bluetooth
Conflicts:		libmate-bluetooth-devel
Conflicts:		libmate-bluetooth-gir1.0
Conflicts:		libmate-bluetooth8

%description
This program enables user to share directories through Webdav.

This package does not provide bluetooth support. Use a generic
tool to get bluetooth support.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
   --disable-scrollkeeper \
   --disable-static \
   --disable-bluetooth \
   --disable-schemas-compile
%make

%install
%makeinstall_std

# remove needless gsettings convert file to avoid slow session start
rm -fr  %{buildroot}%{_datadir}/MateConf

# remove obsolete bluetooth stuff
rm -fr  %{buildroot}%{_sysconfdir}/xdg/autostart/mate-user-share-obex*

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc ChangeLog README
%config(noreplace) %{_sysconfdir}/xdg/autostart/mate-user-share-webdav.desktop
%{_bindir}/mate-file-share-properties
%{_libexecdir}/%{name}
%{_libdir}/caja/
%{_datadir}/%{name}/
%{_datadir}/applications/mate-user-share-properties.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/glib-2.0/schemas/org.mate.FileSharing.gschema.xml
%{_datadir}/help/*/mate-user-share
%{_mandir}/man1/mate-file-share-properties.1*
