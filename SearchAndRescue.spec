#
# TODO:
#	-fix default paths
#	-add data subpackage
#
# Conditional build:
%bcond_with	libY	# build with libY
%bcond_with	jsw		# uild with joystick support
#
%define		shortname searchandrescue
Summary:	Search And Rescue - Linux flight simulator
Summary(pl.UTF-8):	Search And Rescue - symulator lotu śmigłowca
Name:		SearchAndRescue
Version:	1.0.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/project/searchandrescue/Program/SearchAndRescue-1.0.0.tar.gz
# Source0-md5:	3197fe440472e27d36477daaba3b1023
#Patch0: %{name}-Makefile.patch
URL:		http://searchandrescue.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	xorg-xserver-server-devel
%{?with_liby:BuildRequires:	libY-devel}
%{?with_jsw:BuildRequires:	libjsw-devel}
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Linux flight simulator.

%description -l pl.UTF-8
Symulator lotu śmigłowcem.

%prep
%setup -q -n %{shortname}_%{version}
#%patch0 -p1

%build
./configure Linux --prefix=%{_prefix}
%{__make} \
	LDFLAGS="%{rpmldflags}" OPTFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	GAMES_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man6 \
	SHARE_GAMES_DIR=$RPM_BUILD_ROOT%{_datadir} \
	SHADE_ICONS_DIR=$RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS INSTALL README
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/SearchAndRescue.xpm
%{_mandir}/man6/*
