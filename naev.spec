Name:		naev
Version:	0.5.2
Release:	%mkrel 1
Summary:	2D space trading and combat game
Group:		Games/Arcade
License: 	GPLv3+
URL:		http://code.google.com/p/naev/
Source0:	http://naev.googlecode.com/files/%{name}-%{version}.tar.bz2
Source1:	%{name}.png
Source2:	http://naev.googlecode.com/files/ndata-%{version}
Patch1:		naev-0.5.0-linking.patch
Requires:	%{name}-data
BuildRequires:	binutils-devel
BuildRequires:	freetype2-devel
BuildRequires:	jpeg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	mesagl-devel
BuildRequires:	openal-devel
BuildRequires:	png-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	zlib-devel

%description
NAEV is a 2D space trading and combat game, taking inspiration from the
Escape Velocity series.

You pilot a space ship from a top-down perspective, and are more or less
free to do what you want. As the genre name implies, you’re able to trade
and engage in combat at will. Beyond that, there’s an ever-growing number
of storyline missions, equipment, and ships; Even the galaxy itself grows
larger with each release. For the literarily-inclined, there are large
amounts of lore accompanying everything from planets to equipment.

%package	data
Group:		Games/Arcade
License:	GPLv3+ AND GPLv3 AND GPLv2+ AND Public Domain AND CC-by 3.0 AND CC-by-sa 3.0
Summary:	Data files for %{name}
Suggests:	naev
BuildArch:	noarch

%description	data
NAEV is a 2D space trading and combat game, taking inspiration from the
Escape Velocity series.

This is the data file.

%prep
%setup -q
%patch1 -p1 -b .linking

%build
%configure2_5x --with-ndata-path=%{_gamesdatadir}/%{name}/ndata-%{version} --bindir=%{_gamesbindir}
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%__install -m644 %{SOURCE2} -D %{buildroot}%{_gamesdatadir}/%{name}/ndata-%{version}

%__install -m644 %{SOURCE1} -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__mkdir_p %{buildroot}%{_datadir}/applications/
%__cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Naev
GenericName=Naev
Comment=2D space trading and combat game
Icon=%{name}.png
Exec=%{_gamesbindir}/%{name}
Type=Application
Categories=Game;StrategyGame;
StartupNotify=true
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc README LICENSE AUTHORS TODO
%attr(755,root,root) %{_gamesbindir}/%{name}
%{_mandir}/man6/%{name}.6.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/naev-confupdate.sh
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png

%files data
%{_gamesdatadir}/%{name}/ndata-%{version}

