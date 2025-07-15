#
# TODO:
#	- fix default paths
#
# Conditional build:
%bcond_with	libY	# build with libY
%bcond_with	jsw	# uild with joystick support
#
%define		shortname	searchandrescue
%define		data_ver	1.3.0
Summary:	Search And Rescue - Linux flight simulator
Summary(pl.UTF-8):	Search And Rescue - symulator lotu śmigłowca
Name:		SearchAndRescue
Version:	1.3.0
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/searchandrescue/Program/%{name}-%{version}.tar.gz
# Source0-md5:	a3fdc0bf0414a027da7ced635ec5ee25
Source1:	http://downloads.sourceforge.net/searchandrescue/Data_Files/%{name}-data-%{data_ver}.tar.gz
# Source1-md5:	53d6986bd53e7e2b5de0d7bd996a1910
Patch0:		%{name}-flags.patch
Patch1:		%{name}-v3dtex.patch
URL:		http://searchandrescue.sourceforge.net/
BuildRequires:	OpenGL-devel
%{?with_liby:BuildRequires:	libY-devel}
%{?with_jsw:BuildRequires:	libjsw-devel}
BuildRequires:	xorg-xserver-server-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Linux flight simulator.

%description -l pl.UTF-8
Symulator lotu śmigłowcem.

%prep
%setup -q -n %{shortname}_%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
./configure Linux \
	--prefix=%{_prefix}

%{__make} \
	LDFLAGS="%{rpmldflags}" \
	OPTCFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}" \
	OPTCPPFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/%{shortname}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	GAMES_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man6 \
	SHARE_GAMES_DIR=$RPM_BUILD_ROOT%{_datadir} \
	SHADE_ICONS_DIR=$RPM_BUILD_ROOT%{_pixmapsdir}

# unpack data files
tar xvf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/games/%{shortname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS INSTALL README
%attr(755,root,root) %{_bindir}/SearchAndRescue
%{_datadir}/games/%{shortname}
%{_pixmapsdir}/SearchAndRescue.xpm
%{_mandir}/man6/SearchAndRescue.6*
