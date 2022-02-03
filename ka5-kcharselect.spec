%define		kdeappsver	21.12.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kcharselect
Summary:	Kcharselect
Name:		ka5-%{kaname}
Version:	21.12.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	51cf27f8a8a579aad8a4e3355d3a9ba0
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kbookmarks-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KCharSelect is a tool to select special characters from all installed
fonts and copy them into the clipboard.. You can browse characters by
their category or quickly find a certain character by searching for
its name. KCharSelect displays various information about the selected
character.

%description -l pl.UTF-8
KCharSelect jest narzędziem do zaznaczania znaków specjalnych ze
wszystkich zainstalowanych czcionek i kopiowanie ich do schowka.
Możesz przeglądać znaki według kategorii i szybko znaleźć odpowiedni
znak szukając według jego nazwy. KCharSelect wyświetla też różne
informacje o zaznaczonym znaku.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{el,ko,sr}
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
%{_desktopdir}/org.kde.kcharselect.desktop
%{_datadir}/metainfo/org.kde.kcharselect.appdata.xml
