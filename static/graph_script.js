function getBerrySpriteUrl(berryName) {
  return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/" +
    berryName +
    "-berry.png";
}

function getBerryLi(berryName) {
  return "<li><div style='display: flex; align-items: center;'><img src='" +
    getBerrySpriteUrl(berryName) +
    "' height='32px'>" +
    "<span>" +
    berryName +
    "</span>" +
    "</div></li>";
}

function insertBerriesHTMLList(berriesNames) {
  document.getElementById("berriesList").innerHTML =
    berriesNames.map(berryname => getBerryLi(berryname)).join("");
}

function insertPrettyJson(statistics) {
  document.getElementById("prettyJson").textContent = JSON.stringify(statistics, undefined, 4);
}

function insertTotalBerries(total) {
  document.getElementById("totalBerries").textContent = total;
}

function insertAllBerryStatsUrl(allBerryStatsUrl) {
  document.getElementById("allBerryStatsUrl").textContent = allBerryStatsUrl;
}

function createChart(statistics) {
  const statistics_fields = [
    { name: "min_growth_time", color: "#82C24A" },
    { name: "median_growth_time", color: "#4093E9" },
    { name: "max_growth_time", color: "#EF5350" },
    { name: "variance_growth_time", color: "#F7AC2B" },
    { name: "mean_growth_time", color: "#56A3A6" },
    { name: "frequency_growth_time", color: "#B4436C" },
  ];

  const datasets = statistics_fields.map((field, index) => (
    {
      label: "value",
      data: [{ x: index, y: statistics[field.name] }],
      backgroundColor: field.color,
      xAxisID: "x1",
      categoryPercentage: 1,
    }
  ));

  const data = { datasets: datasets };

  const config = {
    type: "bar",
    data,
    options: {
      plugins: {
        legend: false,
        tooltip: {
          callbacks: {
            title(tooltipItems) {
              if (tooltipItems.length) {
                const item = tooltipItems[0];
                const tick = item.chart.scales.x.ticks[item.datasetIndex];
                return tick.label;
              }
            },
          },
        },
      },
      scales: {
        x: {
          labels: ["Min", "Median", "Max", "Variance", "Mean", "Frequency"],
        },
        x1: {
          display: false,
          offset: true,
        },
        y: {
          beginAtZero: true,
          min: 0,
          grid: {
            drawOnChartArea: true,
          },
        },
      },
    },
  };

  const ctx = document.getElementById("myChart");
  const myChart = new Chart(ctx, config);
}

const allBerryStatsUrl = window.location.origin + "/allBerryStats";

async function fetchData() {
  const response = await fetch(allBerryStatsUrl);
  const data = await response.json();

  return data;
}

fetchData().then(statistics => {
  createChart(statistics);
  insertTotalBerries(statistics["berries_names"].length);
  insertBerriesHTMLList(statistics["berries_names"]);
  insertAllBerryStatsUrl(allBerryStatsUrl);
  insertPrettyJson(statistics);
});