#
# Conditiona build
# --with libY - build with libY
# --with jsw - build with lib joystick
#
Summary:	Search And Rescue - Linux flight simulator
Summary(pl):	Search And Rescue - symulator lotu ¶mig³owca
Name:		SearchAndRescue
Version:	0.7d
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}%{version}.tar.bz2
#Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2 (new scheme)
Patch1:		SAR-Makefile.patch
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
%setup -q -n %{name}%{version}
%patch1 -p0

%build
cd sar
#./configure --prefix=%{_prefix}
%{__make} -f Makefile.Linux RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
#%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
