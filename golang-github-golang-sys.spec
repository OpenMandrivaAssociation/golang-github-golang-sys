# http://github.com/golang/sys
%global forgeurl        https://github.com/golang/sys
%global goipath         golang.org/x/sys
%global commit          95b1ffbd15a57cc5abb3f04402b9e8ec0016a52c

%gometa

Name:           golang-github-golang-sys
Version:        0
Release:        0.22%{?dist}
Summary:        Go packages for low-level interaction with the operating system
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{summary}

%package devel
Summary:       %{summary}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgeautosetup

%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d unix

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTING.md README.md AUTHORS CONTRIBUTORS PATENTS

%changelog
* Sat Oct 27 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.22.20181027git95b1ffb
- Bump to commit 95b1ffbd15a57cc5abb3f04402b9e8ec0016a52c

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.git7c87d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.20.git7c87d13
- Upload glide files

* Thu May 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.19.20180517git7c87d13
- Bump to upstream 7c87d13f8e835d2fb3a70a2912c811ed0c1d241b

* Mon Mar 05 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.18.gitf6cff07
- Update to spec 3.0

* Fri Mar 02 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.17.20170302gitf6cff07
- Bump to upstream f6cff0780e542efa0c8e864dc8fa522808f6a598

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.20170302gite48874b
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.gite48874b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.gite48874b
- Bump to upstream e48874b42435b4347fc52bdee0424a52abc974d7
  related: #1360748

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git478fcf5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git478fcf5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.git478fcf5
- Bump to upstream 478fcf54317e52ab69f40bb4c7a1520288d7f7ea
  related: #1360748

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git8f0908a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git8f0908a
- Bump to upstream 8f0908ab3b2457e2e15403d3697c9ef5cb4b57a9
  related: #1360748

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.git62bee03
- Polish the spec file
  related: #1360748

* Wed Aug 17 2016 jchaloup <jchaloup@redhat.com> - 0-0.7.git62bee03
- Bump to upstream 62bee037599929a6e9146f29d10dd5208c43507d
  related: #1360748

* Sat Aug 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.6.git33267e0
- Enable devel and unit-test subpackage for epel7
  related: #1360748

* Tue Aug 02 2016 jchaloup <jchaloup@redhat.com> - 0-0.5.git33267e0
- Bump to upstream 33267e036fd93fcd26ea95b7bdaf2d8306cb743c
  resolves: #1360748

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git9c60d1c
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git9c60d1c
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git9c60d1c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git9c60d1c
- First package for Fedora
  resolves: #1246277

