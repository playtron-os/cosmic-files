Name:           cosmic-files
Version:        1.0.5
Release:        1%{?dist}
Summary:        COSMIC File Manager

License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-files
Source0:        %{name}-%{_arch}.tar.gz

# Runtime dependencies
Requires:       xdg-utils

%description
A file manager for the COSMIC desktop environment.

%prep
%autosetup -n %{name} -p1

%build

%install
# Binaries
install -Dm0755 "usr/bin/cosmic-files" "%{buildroot}%{_bindir}/cosmic-files"
install -Dm0755 "usr/bin/cosmic-files-applet" "%{buildroot}%{_bindir}/cosmic-files-applet"

# Desktop file
install -Dm0644 "usr/share/applications/com.system76.CosmicFiles.desktop" "%{buildroot}%{_datadir}/applications/com.system76.CosmicFiles.desktop"

# Metainfo
install -Dm0644 "usr/share/metainfo/com.system76.CosmicFiles.metainfo.xml" "%{buildroot}%{_datadir}/metainfo/com.system76.CosmicFiles.metainfo.xml"

# Icons
install -Dm0644 "usr/share/icons/hicolor/16x16/apps/com.system76.CosmicFiles.svg" "%{buildroot}%{_datadir}/icons/hicolor/16x16/apps/com.system76.CosmicFiles.svg"
install -Dm0644 "usr/share/icons/hicolor/24x24/apps/com.system76.CosmicFiles.svg" "%{buildroot}%{_datadir}/icons/hicolor/24x24/apps/com.system76.CosmicFiles.svg"
install -Dm0644 "usr/share/icons/hicolor/32x32/apps/com.system76.CosmicFiles.svg" "%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/com.system76.CosmicFiles.svg"
install -Dm0644 "usr/share/icons/hicolor/48x48/apps/com.system76.CosmicFiles.svg" "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/com.system76.CosmicFiles.svg"
install -Dm0644 "usr/share/icons/hicolor/64x64/apps/com.system76.CosmicFiles.svg" "%{buildroot}%{_datadir}/icons/hicolor/64x64/apps/com.system76.CosmicFiles.svg"
install -Dm0644 "usr/share/icons/hicolor/128x128/apps/com.system76.CosmicFiles.svg" "%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/com.system76.CosmicFiles.svg"
install -Dm0644 "usr/share/icons/hicolor/256x256/apps/com.system76.CosmicFiles.svg" "%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/com.system76.CosmicFiles.svg"

# License
install -Dm0644 "usr/share/licenses/cosmic-files/LICENSE" "%{buildroot}%{_datadir}/licenses/cosmic-files/LICENSE"

%files
%license %{_datadir}/licenses/cosmic-files/LICENSE
%{_bindir}/cosmic-files
%{_bindir}/cosmic-files-applet
%{_datadir}/applications/com.system76.CosmicFiles.desktop
%{_datadir}/metainfo/com.system76.CosmicFiles.metainfo.xml
%{_datadir}/icons/hicolor/16x16/apps/com.system76.CosmicFiles.svg
%{_datadir}/icons/hicolor/24x24/apps/com.system76.CosmicFiles.svg
%{_datadir}/icons/hicolor/32x32/apps/com.system76.CosmicFiles.svg
%{_datadir}/icons/hicolor/48x48/apps/com.system76.CosmicFiles.svg
%{_datadir}/icons/hicolor/64x64/apps/com.system76.CosmicFiles.svg
%{_datadir}/icons/hicolor/128x128/apps/com.system76.CosmicFiles.svg
%{_datadir}/icons/hicolor/256x256/apps/com.system76.CosmicFiles.svg

%changelog
* Mon Feb 10 2026 Playtron <dev@playtron.one> - 1.0.5-1
- Initial RPM package for AgentOS
