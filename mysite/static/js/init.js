/*
	Monochromed by TEMPLATED
    templated.co @templatedco
    Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
*/


skel.init({
	prefix: 'css/style',
	resetCSS: true,
	boxModel: 'border',
	grid: {
		gutters: 50
	},
	breakpoints: {
		'mobile': {
			range: '-480',
			lockViewport: true,
			containers: 'fluid',
			grid: {
				collapse: true,
				gutters: 10
			}
		},
		'desktop': {
			range: '481-',
			containers: 1200
		},
		'1000px': {
			range: '481-1200',
			containers: 960
		}
	}
}, {
	panels: {
		panels: {
			navPanel: {
				breakpoints: 'mobile',
				position: 'left',
				style: 'reveal',
				size: '80%',
				html: '<div data-action="navList" data-args="nav"></div>'
			}
		},
		overlays: {
			titleBar: {
				breakpoints: 'mobile',
				position: 'top-left',
				height: 44,
				width: '100%',
				html: '<span class="toggle" data-action="togglePanel" data-args="navPanel"></span>' +
 '<span class="title" data-action="copyHTML" data-args="logo"></span>'
			}
		}
	}
	
	
});

skel.breakpoints({
    skel.breakpoints({
    xlarge: "(max-width: 1680px)",
    large:  "(max-width: 1280px)",
    medium: "(max-width: 980px)",
    small:  "(max-width: 736px)",
    xsmall: "(max-width: 480px)"
});

skel.layout({
    skel.layout({
    reset: "normalize",
    containers: true,
    grid: true,
    breakpoints: {
        medium: {
            containers: "90%"
        },
        small: {
            containers: "95%",
            grid: { gutters: 20 }
        },
        xsmall: {
            grid: { gutters: 10 }
        }
    }
});
});