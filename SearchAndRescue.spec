#
# TODO:
#	-fix default paths
#	-add data subpackage
#
# Conditional build:
%bcond_with	libY	# build with libY
%bcond_with	jsw		# uild with joystick support
#
Summary:	Search And Rescue - Linux flight simulator
Summary(pl):	Search And Rescue - symulator lotu ¶mig³owca
Name:		SearchAndRescue
Version:	0.8.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
# Source0-md5:	e2c56a25adb57554dfb25cc8175b502b
#Patch0:		%{name}-Makefile.patch
URL:		http://wolfpack.twu.net/SearchAndRescue/
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	OpenGL-devel
%{?with_liby:BuildRequires:	libY-devel}
%{?with_jsw:BuildRequires:	libjsw-devel}
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Linux flight simulator.

%description -l pl
Symulator lotu ¶mig³owcem.

%prep
%setup -q
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
