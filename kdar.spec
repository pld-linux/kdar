
%define		_beta	beta3

Summary:	KDar - K Disk archiver
Summary(pl):	KDar - archiwizer dysków K
Name:		kdar
Version:	1.2.0
Release:	0.%{_beta}.1
License:	GPL
Group:		Applications/Archiving
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	cdd78e4dce2ba51b00dce32c03354e49
URL:		http://kdar.sf.net/
#BuildRequires:	attr-devel >= 2.4.16-3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dar-devel >= 2.1.4-1
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	unsermake >= 040511
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K Disk archiver (KDar) is a KDE GUI-based backup and archiving
program. Use it to prepare your data for storage on CD-Rs, jazz
drives, floppies, even DVDs. KDar uses the dar library by Denis
Corbin. Features include compression and archive splitting.

%description -l pl
KDar - archiwizer dysków K jest bazowanym na GUI KDE programem do
backupu i archiwizacji. U¿ywaj go do przygotowania danych maj±cych siê
znale¼æ na p³ytach CD-R, napêdach jazz, dyskietkach, czy nawet DVD.
KDar wykorzystuje bibliotekê dar Denisa Corbina. Pozwala na kompresjê
i podzia³ archiwów.

%prep
%setup -q -n %{name}-%{version}-%{_beta}

%build
cp -f %{_datadir}/automake/config.sub .
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO USAGE
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
#%%{_desktopdir}/*
%{_iconsdir}/*/*/*/*
%{_docdir}/kde/HTML/en/%{name}
