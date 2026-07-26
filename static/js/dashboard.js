/* ==========================================================
   Institutional Brain
   Dashboard Controller

   dashboard.js

========================================================== */

"use strict";

/* ==========================================================
   MAIN OBJECT
========================================================== */

const InstitutionalBrain = {

    initialized: false,

    refreshInterval: 300000,

    init() {

        if (this.initialized) return;

        this.initialized = true;

        this.initializeClock();

        this.initializeCounters();

        this.initializeCards();

        this.initializeTooltips();

        this.initializeLoader();

        this.initializeNotifications();

        console.log("Institutional Brain Initialized");

    }

};


/* ==========================================================
   DOM READY
========================================================== */

document.addEventListener("DOMContentLoaded", function(){

    InstitutionalBrain.init();

});


/* ==========================================================
   LIVE CLOCK
========================================================== */

InstitutionalBrain.initializeClock = function(){

    const clock = document.getElementById("liveClock");

    if(!clock) return;

    function updateClock(){

        const now = new Date();

        clock.innerHTML =
            now.toLocaleDateString() +
            " | " +
            now.toLocaleTimeString();

    }

    updateClock();

    setInterval(updateClock,1000);

};


/* ==========================================================
   COUNTER ANIMATION
========================================================== */

InstitutionalBrain.initializeCounters=function(){

    const counters=document.querySelectorAll(".counter");

    counters.forEach(counter=>{

        const target=parseInt(counter.dataset.target)||0;

        let count=0;

        const speed=Math.max(10,Math.floor(target/100));

        function update(){

            count+=speed;

            if(count>=target){

                counter.innerHTML=target.toLocaleString();

                return;

            }

            counter.innerHTML=count.toLocaleString();

            requestAnimationFrame(update);

        }

        update();

    });

};


/* ==========================================================
   CARD HOVER EFFECT
========================================================== */

InstitutionalBrain.initializeCards=function(){

    const cards=document.querySelectorAll(

        ".analytics-card,.statistics-card,.quick-action-card,.upload-card,.report-card"

    );

    cards.forEach(card=>{

        card.addEventListener("mouseenter",()=>{

            card.style.transform="translateY(-6px)";

        });

        card.addEventListener("mouseleave",()=>{

            card.style.transform="translateY(0px)";

        });

    });

};


/* ==========================================================
   TOOLTIP
========================================================== */

InstitutionalBrain.initializeTooltips=function(){

    const elements=document.querySelectorAll("[data-tooltip]");

    elements.forEach(element=>{

        element.title=element.dataset.tooltip;

    });

};


/* ==========================================================
   LOADER
========================================================== */

InstitutionalBrain.initializeLoader=function(){

    window.showLoader=function(){

        const loader=document.getElementById("loader");

        if(loader){

            loader.style.display="block";

        }

    }

    window.hideLoader=function(){

        const loader=document.getElementById("loader");

        if(loader){

            loader.style.display="none";

        }

    }

};


/* ==========================================================
   TOAST NOTIFICATION
========================================================== */

InstitutionalBrain.initializeNotifications=function(){

    window.showToast=function(message,type="success"){

        let toast=document.createElement("div");

        toast.className="dashboard-toast "+type;

        toast.innerHTML=message;

        document.body.appendChild(toast);

        setTimeout(()=>{

            toast.classList.add("show");

        },100);

        setTimeout(()=>{

            toast.classList.remove("show");

            setTimeout(()=>{

                toast.remove();

            },300);

        },3000);

    }

};
/* ==========================================================
   SIDEBAR CONTROLLER
========================================================== */

InstitutionalBrain.initializeSidebar=function(){

    const sidebar=document.querySelector(".sidebar");

    const toggle=document.getElementById("sidebarToggle");

    if(!sidebar || !toggle) return;

    toggle.addEventListener("click",function(){

        sidebar.classList.toggle("collapsed");

        document.body.classList.toggle("sidebar-collapsed");

        localStorage.setItem(
            "sidebarCollapsed",
            sidebar.classList.contains("collapsed")
        );

    });

    if(localStorage.getItem("sidebarCollapsed")==="true"){

        sidebar.classList.add("collapsed");

        document.body.classList.add("sidebar-collapsed");

    }

};


/* ==========================================================
   FULLSCREEN
========================================================== */

InstitutionalBrain.initializeFullscreen=function(){

    const btn=document.getElementById("fullscreenBtn");

    if(!btn) return;

    btn.addEventListener("click",function(){

        if(!document.fullscreenElement){

            document.documentElement.requestFullscreen();

        }
        else{

            document.exitFullscreen();

        }

    });

};


/* ==========================================================
   DARK MODE (Future Ready)
========================================================== */

InstitutionalBrain.initializeTheme=function(){

    const btn=document.getElementById("themeToggle");

    if(!btn) return;

    if(localStorage.getItem("theme")==="dark"){

        document.body.classList.add("dark-mode");

    }

    btn.addEventListener("click",function(){

        document.body.classList.toggle("dark-mode");

        if(document.body.classList.contains("dark-mode")){

            localStorage.setItem("theme","dark");

        }
        else{

            localStorage.setItem("theme","light");

        }

    });

};


/* ==========================================================
   GLOBAL SEARCH
========================================================== */

InstitutionalBrain.initializeSearch=function(){

    const input=document.getElementById("dashboardSearch");

    if(!input) return;

    input.addEventListener("keyup",function(){

        const value=this.value.toLowerCase();

        document.querySelectorAll(".searchable").forEach(function(item){

            const text=item.innerText.toLowerCase();

            item.style.display=
                text.includes(value)
                ? ""
                : "none";

        });

    });

};


/* ==========================================================
   FILTER CONTROLLER
========================================================== */

InstitutionalBrain.initializeFilters=function(){

    const filters=document.querySelectorAll(".dashboard-filter");

    filters.forEach(filter=>{

        filter.addEventListener("change",function(){

            InstitutionalBrain.applyFilters();

        });

    });

};


InstitutionalBrain.applyFilters=function(){

    console.log("Dashboard filters updated");

    showToast("Dashboard filters applied.","info");

};


/* ==========================================================
   USER DROPDOWN
========================================================== */

InstitutionalBrain.initializeUserMenu=function(){

    const btn=document.getElementById("userMenuButton");

    const menu=document.getElementById("userMenu");

    if(!btn || !menu) return;

    btn.addEventListener("click",function(e){

        e.stopPropagation();

        menu.classList.toggle("show");

    });

    document.addEventListener("click",function(){

        menu.classList.remove("show");

    });

};


/* ==========================================================
   SESSION KEEP ALIVE
========================================================== */

InstitutionalBrain.initializeSession=function(){

    setInterval(function(){

        fetch("/dashboard/session/keepalive/",{

            method:"GET",

            credentials:"same-origin"

        }).catch(function(){

            console.log("Session refresh failed.");

        });

    },600000);

};


/* ==========================================================
   KEYBOARD SHORTCUTS
========================================================== */

InstitutionalBrain.initializeKeyboard=function(){

    document.addEventListener("keydown",function(e){

        if(e.ctrlKey && e.key==="f"){

            e.preventDefault();

            const search=document.getElementById("dashboardSearch");

            if(search){

                search.focus();

            }

        }

        if(e.key==="Escape"){

            document.querySelectorAll(".modal.show").forEach(function(modal){

                modal.classList.remove("show");

            });

        }

    });

};


/* ==========================================================
   AUTO REFRESH TIMER
========================================================== */

InstitutionalBrain.initializeAutoRefresh=function(){

    setInterval(function(){

        console.log("Refreshing dashboard...");

        InstitutionalBrain.refreshDashboard();

    },InstitutionalBrain.refreshInterval);

};


InstitutionalBrain.refreshDashboard=function(){

    console.log("Dashboard refreshed.");

};


/* ==========================================================
   UPDATE INIT
========================================================== */

const originalInit=InstitutionalBrain.init;

InstitutionalBrain.init=function(){

    originalInit.call(this);

    this.initializeSidebar();

    this.initializeFullscreen();

    this.initializeTheme();

    this.initializeSearch();

    this.initializeFilters();

    this.initializeUserMenu();

    this.initializeSession();

    this.initializeKeyboard();

    this.initializeAutoRefresh();

};
/* ==========================================================
   CHART.JS CONTROLLER
========================================================== */

InstitutionalBrain.charts = {};


/* ==========================================================
   INITIALIZE ALL CHARTS
========================================================== */

InstitutionalBrain.initializeCharts = function(){

    this.initializeDepartmentChart();

    this.initializeNAACChart();

    this.initializeNBAChart();

    this.initializeNIRFChart();

    this.initializeResearchChart();

    this.initializeRiskChart();

    this.initializeFacultyChart();

    this.initializeStudentChart();

};


/* ==========================================================
   COMMON CHART OPTIONS
========================================================== */

InstitutionalBrain.chartOptions = {

    responsive:true,

    maintainAspectRatio:false,

    animation:{
        duration:1200
    },

    plugins:{

        legend:{
            position:"bottom"
        }

    }

};


/* ==========================================================
   DEPARTMENT PERFORMANCE
========================================================== */

InstitutionalBrain.initializeDepartmentChart=function(){

    const canvas=document.getElementById("departmentChart");

    if(!canvas) return;

    this.charts.department=new Chart(canvas,{

        type:"bar",

        data:{

            labels:[
                "CSE",
                "ECE",
                "ME",
                "CE",
                "MBA",
                "Math"
            ],

            datasets:[{

                label:"Performance",

                data:[91,84,79,86,89,94]

            }]

        },

        options:this.chartOptions

    });

};


/* ==========================================================
   NAAC
========================================================== */

InstitutionalBrain.initializeNAACChart=function(){

    const canvas=document.getElementById("naacChart");

    if(!canvas) return;

    this.charts.naac=new Chart(canvas,{

        type:"radar",

        data:{

            labels:[

                "C1",

                "C2",

                "C3",

                "C4",

                "C5",

                "C6",

                "C7"

            ],

            datasets:[{

                label:"NAAC Score",

                data:[92,88,84,90,93,95,89]

            }]

        },

        options:this.chartOptions

    });

};


/* ==========================================================
   NBA
========================================================== */

InstitutionalBrain.initializeNBAChart=function(){

    const canvas=document.getElementById("nbaChart");

    if(!canvas) return;

    this.charts.nba=new Chart(canvas,{

        type:"line",

        data:{

            labels:[

                "PO1",

                "PO2",

                "PO3",

                "PO4",

                "PO5",

                "PO6"

            ],

            datasets:[{

                label:"Attainment",

                data:[81,84,86,82,90,93],

                tension:.4

            }]

        },

        options:this.chartOptions

    });

};


/* ==========================================================
   NIRF
========================================================== */

InstitutionalBrain.initializeNIRFChart=function(){

    const canvas=document.getElementById("nirfChart");

    if(!canvas) return;

    this.charts.nirf=new Chart(canvas,{

        type:"doughnut",

        data:{

            labels:[

                "TLR",

                "RP",

                "GO",

                "OI",

                "PR"

            ],

            datasets:[{

                data:[28,22,20,15,15]

            }]

        },

        options:this.chartOptions

    });

};


/* ==========================================================
   RESEARCH
========================================================== */

InstitutionalBrain.initializeResearchChart=function(){

    const canvas=document.getElementById("researchChart");

    if(!canvas) return;

    this.charts.research=new Chart(canvas,{

        type:"line",

        data:{

            labels:[

                "2022",

                "2023",

                "2024",

                "2025",

                "2026"

            ],

            datasets:[{

                label:"Publications",

                data:[45,63,88,111,145],

                tension:.35

            }]

        },

        options:this.chartOptions

    });

};


/* ==========================================================
   RISK ANALYSIS
========================================================== */

InstitutionalBrain.initializeRiskChart=function(){

    const canvas=document.getElementById("riskChart");

    if(!canvas) return;

    this.charts.risk=new Chart(canvas,{

        type:"polarArea",

        data:{

            labels:[

                "Academic",

                "Research",

                "Finance",

                "Infrastructure",

                "Compliance"

            ],

            datasets:[{

                data:[18,12,9,7,4]

            }]

        },

        options:this.chartOptions

    });

};


/* ==========================================================
   FACULTY
========================================================== */

InstitutionalBrain.initializeFacultyChart=function(){

    const canvas=document.getElementById("facultyChart");

    if(!canvas) return;

    this.charts.faculty=new Chart(canvas,{

        type:"bar",

        data:{

            labels:[

                "Teaching",

                "Research",

                "Projects",

                "Patents",

                "Extension"

            ],

            datasets:[{

                label:"Faculty KPI",

                data:[88,74,69,53,81]

            }]

        },

        options:this.chartOptions

    });

};


/* ==========================================================
   STUDENT
========================================================== */

InstitutionalBrain.initializeStudentChart=function(){

    const canvas=document.getElementById("studentChart");

    if(!canvas) return;

    this.charts.student=new Chart(canvas,{

        type:"pie",

        data:{

            labels:[

                "Excellent",

                "Good",

                "Average",

                "Need Improvement"

            ],

            datasets:[{

                data:[32,41,20,7]

            }]

        },

        options:this.chartOptions

    });

};


/* ==========================================================
   REFRESH CHARTS
========================================================== */

InstitutionalBrain.refreshCharts=function(){

    Object.values(this.charts).forEach(chart=>{

        if(chart){

            chart.update();

        }

    });

};


/* ==========================================================
   UPDATE INIT
========================================================== */

const previousInit=InstitutionalBrain.init;

InstitutionalBrain.init=function(){

    previousInit.call(this);

    this.initializeCharts();

};
/* ==========================================================
   API CONFIGURATION
========================================================== */

InstitutionalBrain.api={

    summary:"/dashboard/api/summary/",

    charts:"/dashboard/api/charts/",

    departments:"/dashboard/api/departments/",

    faculty:"/dashboard/api/faculty/",

    students:"/dashboard/api/students/",

    research:"/dashboard/api/research/",

    naac:"/dashboard/api/naac/",

    nba:"/dashboard/api/nba/",

    nirf:"/dashboard/api/nirf/",

    risk:"/dashboard/api/risk/",

    reports:"/dashboard/api/reports/"

};


/* ==========================================================
   GENERIC FETCH
========================================================== */

InstitutionalBrain.fetchData=async function(url){

    try{

        showLoader();

        const response=await fetch(url,{

            credentials:"same-origin",

            headers:{
                "X-Requested-With":"XMLHttpRequest"
            }

        });

        if(!response.ok){

            throw new Error(response.status);

        }

        return await response.json();

    }

    catch(error){

        console.error(error);

        showToast("Unable to load dashboard data.","danger");

        return null;

    }

    finally{

        hideLoader();

    }

};
/* ==========================================================
   AI REPORT GENERATION
========================================================== */

InstitutionalBrain.generateAIReport = async function(type){

    try{

        showLoader();

        const response = await fetch(

            "/dashboard/api/ai-report/",

            {

                method:"POST",

                headers:{

                    "Content-Type":"application/json",

                    "X-CSRFToken":this.getCSRFToken()

                },

                body:JSON.stringify({

                    report:type

                })

            }

        );

        const result = await response.json();

        hideLoader();

        showToast("AI Report Generated Successfully","success");

        if(result.url){

            window.open(result.url,"_blank");

        }

    }

    catch(error){

        hideLoader();

        showToast("Unable to generate report.","danger");

    }

};


/* ==========================================================
   EXPORT
========================================================== */

InstitutionalBrain.exportDashboard=function(format){

    window.location=

    "/dashboard/export/?format="+format;

};


/* ==========================================================
   EXPORT CURRENT CHART
========================================================== */

InstitutionalBrain.exportChart=function(chartName){

    const chart=this.charts[chartName];

    if(!chart) return;

    const link=document.createElement("a");

    link.href=chart.toBase64Image();

    link.download=chartName+".png";

    link.click();

};


/* ==========================================================
   SAVE FILTERS
========================================================== */

InstitutionalBrain.saveFilters=function(){

    const filters={};

    document.querySelectorAll(".dashboard-filter").forEach(function(item){

        filters[item.id]=item.value;

    });

    localStorage.setItem(

        "dashboardFilters",

        JSON.stringify(filters)

    );

};


/* ==========================================================
   LOAD FILTERS
========================================================== */

InstitutionalBrain.loadFilters=function(){

    const saved=

    JSON.parse(

        localStorage.getItem("dashboardFilters")||"{}"

    );

    Object.keys(saved).forEach(function(id){

        const control=document.getElementById(id);

        if(control){

            control.value=saved[id];

        }

    });

};


/* ==========================================================
   ERROR LOGGER
========================================================== */

window.onerror=function(message,file,line){

    console.error(

        message,

        file,

        line

    );

};


/* ==========================================================
   PERFORMANCE MONITOR
========================================================== */

InstitutionalBrain.performance=function(){

    console.log(

        "Dashboard Loaded:",

        performance.now().toFixed(2),

        "ms"

    );

};


/* ==========================================================
   HEALTH CHECK
========================================================== */

InstitutionalBrain.healthCheck=async function(){

    try{

        const response=

        await fetch(

            "/dashboard/api/health/"

        );

        if(response.ok){

            console.log("Dashboard Healthy");

        }

    }

    catch{

        showToast(

            "Server Connection Lost",

            "warning"

        );

    }

};


/* ==========================================================
   NOTIFICATION CENTER
========================================================== */

InstitutionalBrain.notifications=function(){

    fetch("/dashboard/api/notifications/")

    .then(r=>r.json())

    .then(data=>{

        const badge=

        document.getElementById(

            "notificationCount"

        );

        if(badge){

            badge.innerHTML=data.count;

        }

    });

};


/* ==========================================================
   AUTO SAVE
========================================================== */

setInterval(function(){

    InstitutionalBrain.saveFilters();

},30000);


/* ==========================================================
   HEALTH CHECK
========================================================== */

setInterval(function(){

    InstitutionalBrain.healthCheck();

},120000);


/* ==========================================================
   NOTIFICATIONS
========================================================== */

setInterval(function(){

    InstitutionalBrain.notifications();

},60000);


/* ==========================================================
   CSRF TOKEN
========================================================== */

InstitutionalBrain.getCSRFToken=function(){

    const token=

    document.querySelector(

        "[name=csrfmiddlewaretoken]"

    );

    return token?token.value:"";

};


/* ==========================================================
   UTILITIES
========================================================== */

InstitutionalBrain.formatNumber=function(value){

    return Number(value).toLocaleString();

};


InstitutionalBrain.formatPercent=function(value){

    return value+"%";

};


InstitutionalBrain.randomColor=function(){

    return "#"+Math.floor(

        Math.random()*16777215

    ).toString(16);

};


/* ==========================================================
   FINAL INITIALIZATION
========================================================== */

const previousInitialization=

InstitutionalBrain.init;

InstitutionalBrain.init=function(){

    previousInitialization.call(this);

    this.loadFilters();

    this.performance();

    this.notifications();

    this.healthCheck();

};
