%define bname qalculate

Summary:	A very versatile desktop calculator
Name:		%{bname}-gtk
Version:	5.6.0
Release:	1
License:	GPLv2+
Group:		Office
Url:		https://qalculate.github.io/
Source0:	https://github.com/Qalculate/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	gmp-devel
BuildRequires:	intltool
BuildRequires:	imagemagick
BuildRequires:	rarian
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libqalculate)
BuildRequires:  pkgconfig(mpfr)
Requires(pre):	rarian
Requires:	gnuplot

%description
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is small
and simple to use but with much power and versatility underneath

Features include customizable functions, units, arbitrary precision,
plotting, and a user-friendly interface.

This package provides the GTK+ frontend.

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%doc doc/html
%{_bindir}/*
%{_libexecdir}/qalculate-search-provider
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/dbus-1/services/io.github.Qalculate.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/io.github.Qalculate.search-provider.ini
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*/apps/qalculate.{svg,png}
%{_mandir}/man1/%{name}.1.*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

# locales
%find_lang %{name} --with-gnome

