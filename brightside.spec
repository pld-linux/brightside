Summary:	Brightside Screen Corners and Edges daemon
Summary(pl):	Brightside - demon rogów i krawêdzi ekranu
Name:		brightside
Version:	1.4.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://files.catmur.co.uk/brightside/%{name}-%{version}.tar.bz2
# Source0-md5:	eed041f45dfa5f29796fde9e302d68c6
Patch0:		%{name}-wnck_workspace_activate.patch
Patch1:		%{name}-gconf-mouse-speed.patch
URL:		http://wiki.catmur.co.uk/Brightside
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libwnck-devel
Requires(post,preun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Brightside is a tool to add reactivity to the corners and edges of
your GNOME desktop.

Brightside provides edge flipping to allow you to switch to the
adjacent workspace simply by pressing your mouse against the edge of
the screen.

Brightside also allows you to assign configurable actions to occur
while you rest the mouse in a corner of the screen. Currently
available actions comprise:

- Fade out volume
- Prevent screensaver starting
- Start screensaver and lock screen
- Enter DPMS standby mode
- Enter DPMS suspend mode
- Enter DPMS off mode
- Dim laptop backlight
- Custom action

%description -l pl
Brightside to narzêdzie dodaj±ce reaktywno¶æ rogom i krawêdziom
pulpitu GNOME.

Brightside udostêpnia zamianê krawêdzi pozwalaj±c± prze³±czyæ siê na
s±siednie biurko poprzez samo naci¶niêcie przycisku myszy na krawêdzi
ekranu.

Brightside pozwala tak¿e przypisywaæ ró¿ne konfigurowalne akcje maj±ce
zaj¶æ kiedy mysz pozostaje w rogu ekranu. Aktualnie dostêpne akcje
obejmuj±:
- wyciszenie d¼wiêku
- zapobieganie w³±czeniu wygaszacza ekranu
- uruchomienie wygaszacza i zablokowanie ekranu
- wej¶cie w tryb DPMS standby
- wej¶cie w tryb DPMS suspend
- wej¶cie w tryb DPMS off
- przyciemnienie pod¶wietlenia wy¶wietlacza w laptopie
- akcje zdefiniowane przez u¿ytkownika

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-dependency-tracking \
	--enable-tray-icon

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{name}.schemas

%preun
%gconf_schema_uninstall %{name}.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
