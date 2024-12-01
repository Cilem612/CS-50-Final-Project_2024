// Update flight times
function updateFlightTimes() {
    const timeElements = document.querySelectorAll('.flight-time');
    timeElements.forEach(element => {
        const timestamp = element.getAttribute('data-time');
        if (timestamp) {
            element.textContent = formatDateTime(timestamp);
        }
    });
  }
  
  // Format datetime
  function formatDateTime(timestamp) {
    const date = new Date(timestamp);
    return date.toLocaleString('en-US', {
        hour: '2-digit',
        minute: '2-digit',
        day: '2-digit',
        month: 'short',
        year: 'numeric'
    });
  }
  
  // Format remaining time
  function formatRemainingTime(minutes) {
    if (minutes < 0) return 'Departed';
    if (minutes < 60) return `${minutes}m`;
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    return `${hours}h ${mins}m`;
  }
  
  // Search functionality
  function initializeSearch() {
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('input', debounce(handleSearch, 300));
    }
  }
  
  // Handle search
  async function handleSearch(event) {
    const searchTerm = event.target.value.trim();
    const resultsContainer = document.getElementById('searchResults');
    
    if (!searchTerm || searchTerm.length < 2) {
        resultsContainer.innerHTML = '';
        return;
    }
    
    try {
        const response = await fetch(`/search?q=${encodeURIComponent(searchTerm)}`);
        const data = await response.json();
        displaySearchResults(data, resultsContainer);
    } catch (error) {
        console.error('Search error:', error);
        resultsContainer.innerHTML = `
            <div class="alert alert-danger dark-mode-element">
                Error performing search. Please try again.
            </div>`;
    }
  }
  
  // Display search results
  function displaySearchResults(flights, container) {
    if (flights.length === 0) {
        container.innerHTML = `
            <div class="alert alert-info dark-mode-element">
                No flights found matching your search.
            </div>`;
        return;
    }
    
    const resultsHTML = flights.map(flight => `
        <div class="card mb-2 dark-mode-element">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <h5 class="card-title mb-1">Flight ${flight.flight_number}</h5>
                        <p class="card-text mb-0">
                            ${flight.departure} → ${flight.arrival}<br>
                            <small class="text-muted">
                                Departure: ${flight.departure_time}
                            </small>
                        </p>
                    </div>
                    <a href="/flight/${flight.id}" class="btn btn-primary btn-sm">
                        View Details
                    </a>
                </div>
            </div>
        </div>
    `).join('');
    
    container.innerHTML = resultsHTML;
  }
  
  // Debounce function to limit API calls
  function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
  }
  
  // Initialize when page loads
  document.addEventListener('DOMContentLoaded', () => {
    updateFlightTimes();
    initializeSearch();
    setInterval(updateFlightTimes, 60000);
  });
  document.addEventListener('DOMContentLoaded', function () {
    // Enable dark mode by adding the class 'dark-mode' to the body
    document.body.classList.add('dark-mode');
});
