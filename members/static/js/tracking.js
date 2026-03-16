function getVisitorId() {
    let id = localStorage.getItem("visitor_id");

    if (!id) {
        id = "v_" + Math.random().toString(36).substr(2, 9);
        localStorage.setItem("visitor_id", id);
    }

    return id;
}

const visitorData = {

visitor_id: getVisitorId(),
session_id: Date.now(),

page_url: window.location.href,
page_title: document.title,
referrer: document.referrer,

screen_width: screen.width,
screen_height: screen.height,

language: navigator.language,
timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,

user_agent: navigator.userAgent

};

fetch("/track-visitor2/", {
method: "POST",
headers: {
"Content-Type": "application/json"
},
body: JSON.stringify(visitorData)
});