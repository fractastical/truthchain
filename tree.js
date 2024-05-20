const width = 600;
const height = 600;
const assertions = [
    "This is assertion 1",
    "This is assertion 2",
    "This is assertion 3",
    "This is assertion 4",
    "This is assertion 5"
];

const svg = d3.select("#fern")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

const g = svg.append("g")
    .attr("transform", "translate(" + width / 2 + "," + height + ")");

function drawFern() {
    const numPoints = 50000;
    const points = generateFernPoints(numPoints);

    g.selectAll("circle")
        .data(points)
        .enter()
        .append("circle")
        .attr("cx", d => d[0])
        .attr("cy", d => d[1])
        .attr("r", 0.5)
        .style("fill", "#007f00")
        .on("mouseover", function (event, d) {
            const idx = Math.floor(Math.random() * assertions.length);
            d3.select(this)
                .attr("r", 2)
                .style("fill", "#ff0000")
                .append("title")
                .text(assertions[idx]);
        })
        .on("mouseout", function () {
            d3.select(this)
                .attr("r", 0.5)
                .style("fill", "#007f00");
        });
}

function generateFernPoints(numPoints) {
    let x = 0, y = 0;
    const points = [];

    for (let i = 0; i < numPoints; i++) {
        const nextPoint = getNextPoint(x, y);
        x = nextPoint[0];
        y = nextPoint[1];
        points.push([width / 2 + x * 50, height - y * 50]);
    }

    return points;
}

function getNextPoint(x, y) {
    const r = Math.random();
    if (r < 0.01) {
        return [0, 0.16 * y];
    } else if (r < 0.86) {
        return [0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6];
    } else if (r < 0.93) {
        return [0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6];
    } else {
        return [-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44];
    }
}

drawFern();
