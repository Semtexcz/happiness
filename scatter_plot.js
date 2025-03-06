document.addEventListener("DOMContentLoaded", function () {
    const chart = Highcharts.chart("chart-container", {
        chart: {
            type: "scatter",
            zoomType: "xy",
            backgroundColor: "#f4f4f4",
            width: 500,
            height: 500
        },
        title: {
            text: "Hodnocení činností - Smysluplnost vs. Zábavnost"
        },
        xAxis: {
            title: {
                text: "Smysluplnost (-5 až 5)"
            },
            min: -5,
            max: 5,
            gridLineWidth: 1
        },
        yAxis: {
            title: {
                text: "Zábavnost (-5 až 5)"
            },
            min: -5,
            max: 5,
            gridLineWidth: 1
        },
        tooltip: {
            formatter: function () {
                return `<b>${this.point.name}</b><br>Smysluplnost: ${this.x}<br>Zábavnost: ${this.y}`;
            }
        },
        series: [{
            name: "Činnosti",
            color: "rgba(223, 83, 83, .5)",
            data: [
                { x: 5, y: 5, name: "Sex / Intimní aktivity" },
                { x: 3, y: 4, name: "Společenské aktivity (socializace)" },
                { x: 2, y: 4, name: "Fyzická aktivita (cvičení)" },
                { x: 5, y: 1, name: "Dobrovolnictví a péče o druhé" },
                { x: 4, y: 0, name: "Duchovní aktivity" },
                { x: 2, y: 2, name: "Hobby a koníčky" },
                { x: 0, y: 3, name: "Relaxace a odpočinek" },
                { x: 0, y: 3, name: "Jídlo" },
                { x: -1, y: 4, name: "Pití alkoholu / Party" },
                { x: 4, y: -2, name: "Studium / školení" },
                { x: -1, y: 3, name: "Hraní videoher" },
                { x: 3, y: -1, name: "Placená práce" },
                { x: -2, y: 2, name: "Nakupování pro radost" },
                { x: -1, y: -3, name: "Domácí práce" },
                { x: -2, y: -3, name: "Osobní hygiena" },
                { x: -3, y: -4, name: "Dojíždění" },
                { x: -4, y: -3, name: "Používání sociálních sítí" },
                { x: -4, y: -4, name: "Být nemocný" }
            ]
        }]
    });
});
