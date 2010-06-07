#
# Conditional build:
%bcond_with	libY	# build with libY
%bcond_with	jsw	# uild with joystick support
#
%define		shortname searchandrescue
Summary:	Search And Rescue - Linux flight simulator
Summary(pl.UTF-8):	Search And Rescue - symulator lotu śmigłowca
Name:		SearchAndRescue
Version:	1.0.0
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/searchandrescue/Program/%{name}-%{version}.tar.gz
# Source0-md5:	3197fe440472e27d36477daaba3b1023
Source1:	http://downloads.sourceforge.net/searchandrescue/Data_Files/%{name}-data-%{version}.tar.gz
# Source1-md5:	da92f5fa7587cc0a712706d01b2f59f1
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

%build
./configure Linux --prefix=%{_prefix}
%{__make} \
	LDFLAGS="%{rpmldflags}" OPTFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"

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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/%{shortname}
#%%{_iconsdir}/SearchAndRescue.xpm
%{_mandir}/man6/*
