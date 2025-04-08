import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://effective-fiesta-x5r7qpjwx559hrw5-8000.app.github.dev/api/activities/')
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div>
      <h1 className="text-center text-primary">Activities</h1>
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th>Activity Type</th>
            <th>Duration (minutes)</th>
          </tr>
        </thead>
        <tbody>
          {activities.map(activity => (
            <tr key={activity.id}>
              <td>{activity.activity_type}</td>
              <td>{activity.duration}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
