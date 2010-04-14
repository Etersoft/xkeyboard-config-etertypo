Name: typo
Version: 1.0
Release: alt1

Summary: Typographic layout for X11
License: GPL
Group: System/X11

Url: http://regolit.com/2006/11/26/xkb-unicode/

Packager: Devaev Maxim <mdevaev@etersoft.ru>

# http://git.etersoft.ru/people/mdevaev/packages/typo.git
Source: %name-%version.tar

BuildArchitectures: noarch
BuildRequires: rpm-build-compat

%description
Typographic layout for X11

%prep
%setup

%install
mkdir -p %buildroot%_datadir/X11/xkb/symbols
mkdir -p %buildroot%_docdir/typo
cp -f typo/symbols_typo %buildroot%_datadir/X11/xkb/symbols/typo
cp -f typo/README %buildroot%_docdir/typo
cp -f typo/xkb-typo-scheme.png %buildroot%_docdir/typo

%files
%buildroot%_datadir/X11/xkb/symbols/typo
%buildroot%_docdir/typo/*

%changelog
* Wed Apr 14 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt1
- Initial build

