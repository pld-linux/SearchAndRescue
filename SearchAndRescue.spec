#
# TODO: fix default paths
#
# Conditional build:
# --with libY	- with libY
# --with jsw	- with lib joystick
#
Summary:	Search And Rescue - Linux flight simulator
Summary(pl):	Search And Rescue - symulator lotu ¶mig³owca
Name:		SearchAndRescue
Version:	0.7.20
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
Patch0:		%{name}-Makefile.patch
URL:		http://wolfpack.twu.net/SearchAndRescue/
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	OpenGL-devel
%{?_with_liby:BuildRequires: libY-devel}
%{?_with_jsw:BuildRequires:	libjsw-devel}
Requires:	OpenGL
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Linux flight simulator.

%description -l pl
Symulator lotu ¶mig³owcem.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%{__make} -C sar -f Makefile.Linux \
	OPTFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C sar -f Makefile.Linux install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	GAMES_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man6 \
	SHARE_GAMES_DIR=$RPM_BUILD_ROOT%{_datadir} \
	SHADE_ICONS_DIR=$RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS INSTALL README docs
%attr(755,root,root) %{_bindir}/*
%{_datadir}/SearchAndRescue
%{_pixmapsdir}/SearchAndRescue.xpm
%{_mandir}/man6/*
