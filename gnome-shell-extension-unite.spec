%global extuuid		unite@hardpixel.eu
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		unite-shell
%global giturl		https://github.com/hardpixel/%{gitname}
Name:		gnome-shell-extension-unite
Version:	71
Release:	1%{?dist}
Summary:	GNOME Shell Extension Unite by hardpixel

License:	GPLv3+
URL:		%{giturl}
Source0:	%{giturl}/archive/v%{version}.tar.gz#/%{gitname}-%{version}.tar.gz

BuildArch:	noarch


%description
Unite is a GNOME Shell extension which makes a few layout tweaks to the
top panel and removes window decorations to make it look like Ubuntu
Unity Shell.

  * Adds window buttons to the top panel for maximized windows.
  * Shows current window title in the app menu for maximized windows.
  * Removes titlebars on maximized windows.
  * Hides window controls on maximized windows with headerbars.
  * Moves the date to the right, fixes icons spacing and removes
    dropdown arrows.
  * Moves legacy tray icons to the top panel.
  * Moves notifications to the right.
  * Hides activities button.


%prep
%autosetup -n %{gitname}-%{version} -p 1


%build
# noop


%install
%{__mkdir} -p %{buildroot}%{extdir}
%{__cp} -pr %{extuuid}/* %{buildroot}%{extdir}


%files
%license LICENSE
%doc README.md
%{extdir}
%dir %{_datadir}/gnome-shell/extensions/
%dir %{_datadir}/gnome-shell/

%changelog
