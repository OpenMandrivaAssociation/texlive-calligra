# revision 15878
# category Package
# catalog-ctan /fonts/calligra
# catalog-date 2010-05-03 23:11:16 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-calligra
Version:	20100503
Release:	10
Summary:	Calligraphic font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/calligra
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calligra.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calligra.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A calligraphic font in the handwriting style of the author,
Peter Vanroose. The font is supplied as MetaFont source LaTeX
support of the font is provided in the calligra package in the
fundus bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/calligra/callig15.mf
%{_texmfdistdir}/fonts/source/public/calligra/calligra.mf
%{_texmfdistdir}/fonts/tfm/public/calligra/callig15.tfm
%doc %{_texmfdistdir}/doc/latex/calligra/README
%doc %{_texmfdistdir}/doc/latex/calligra/testfont.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100503-2
+ Revision: 749951
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100503-1
+ Revision: 717995
- texlive-calligra
- texlive-calligra
- texlive-calligra
- texlive-calligra
- texlive-calligra

