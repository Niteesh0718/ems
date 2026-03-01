fetch("http://127.0.0.1:8000/get_events/")
.then((res)=>res.json())
.then(events => {
    const container = document.getElementById("events-container");

    events.forEach(e => {
      const card = document.createElement("a");

     
      card.href = `/ems_dashboard/event/${e.id}/`;   

      card.className = "event-card-link";

      card.innerHTML = `
        <div class="event-card">
          <img src="${e.img_url || 'https://via.placeholder.com/300x200'}">
          <div class="event-info">
            <div class="event-name">${e.event_name}</div>
            <div class="event-meta">${e.date} • ${e.time}</div>
            <div class="event-meta">${e.venue}</div>
          </div>
        </div>
      `;

      container.appendChild(card);
    });
  });