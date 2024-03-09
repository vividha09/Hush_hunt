import React, { useState } from "react";
import Calendar from "react-calendar";
import "react-calendar/dist/Calendar.css"; // Import default styles
import "./Calendar.css"; // Import custom CSS if needed
import image1 from "../images/flipkart.jpg"; // Import image 1
import image2 from "../images/flipkart.jpg"; // Import image 2

const MyCalendar = () => {
  const [date, setDate] = useState(new Date());
  const [events, setEvents] = useState([
    { date: "2024-03-10", title: "Event 1", photoUrl: image1 }, // Use imported image
    { date: "2024-03-15", title: "Event 2", photoUrl: image2 }, // Use imported image
  ]);

  const onChange = (selectedDate) => {
    setDate(selectedDate);
  };

  const renderEventsForDate = (date) => {
    const eventsForDate = events.filter(
      (event) => event.date === date.toISOString().split("T")[0]
    );
    return eventsForDate.map((event) => (
      <div key={event.title}>
        <h3>{event.title}</h3>
        <img src={event.photoUrl} alt={event.title} /> {/* Use relative path */}
      </div>
    ));
  };

  return (
    <div className="calendar-container">
      <Calendar
        onChange={onChange}
        value={date}
        tileContent={({ date }) => renderEventsForDate(date)}
      />
    </div>
  );
};

export default MyCalendar;
