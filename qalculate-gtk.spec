%define bname qalculate

Summary:	A very versatile desktop calculator
Name:		qalculate-gtk
Version:	0.9.6
Release:	%mkrel 1
License:	GPL
Group:		Office
URL:		http://qalculate.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/qalculate/%{name}-%{version}.tar.bz2
BuildRequires:	libqalculate-devel >= %{version} 
BuildRequires:	libglade2.0-devel
BuildRequires:	gtk+2-devel
BuildRequires:	imagemagick
BuildRequires:	scrollkeeper
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
Requires(pre):	scrollkeeper
Requires:	gnuplot
Requires:	wget
Obsoletes:	qalculate
Provides:	qalculate

%description
Qalculate! is a modern multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting,
and a graphical interface that uses a one-line fault-tolerant expression entry 
(although it supports optional traditional buttons). 
This package provides the GTK frontend.
 
%prep
%setup -q 
 
%build

%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

#menu
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps

#icons 
convert -size 48x48 data/%{bname}.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png 
convert -size 32x32 data/%{bname}.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png 
convert -size 16x16 data/%{bname}.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

desktop-file-install --vendor="" \
--remove-category="Application" \
--add-category="GTK" \
--add-category="Calculator" \
--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/* 

##CAE rm symlink so both gtk and kde frontend are installable
rm -f %{buildroot}%{_bindir}/qalculate

%find_lang %{name} --with-gnome

%clean
rm -rf %{buildroot}

%post
%{update_menus}
%update_scrollkeeper
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_scrollkeeper
%clean_icon_cache hicolor
 
%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/gnome/help/%{name}
%{_datadir}/omf/%{name}
%exclude %{_datadir}/pixmaps/*.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade/*.glade
%{_iconsdir}/hicolor/*/apps/%{name}.png
