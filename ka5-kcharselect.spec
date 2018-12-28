%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kcharselect
Summary:	Kcharselect
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	4e9c601f2f5fd5212e8e48032f6cc4aa
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kbookmarks-devel >= 5.25.0
BuildRequires:	kf5-kcrash-devel >= 5.25.0
BuildRequires:	kf5-kdoctools-devel >= 5.25.0
BuildRequires:	kf5-ki18n-devel >= 5.25.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.25.0
BuildRequires:	kf5-kxmlgui-devel >= 5.25.0
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

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
%{_desktopdir}/org.kde.kcharselect.desktop
%{_datadir}/metainfo/org.kde.kcharselect.appdata.xml
