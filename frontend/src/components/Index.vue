<template>
  <div class="small container">
    <div class="columns">
      <div class="column">
        <div class="field is-grouped is-grouped-centered">
          <label class="label">Tipo de cambio</label>
        </div>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <div class="field is-grouped is-grouped-centered">
          <p class="control">
            <span class="select">
              <select v-model="currency">
                <option value="UDI">UDI's</option>
                <option value="USD" selected>USD</option>
                <option value="TIIE">TIIE</option>
              </select>
            </span>
          </p>
        </div>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <div class="field is-grouped is-grouped-centered">
          <label class="label">Fecha</label>
        </div>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <div class="field is-grouped is-grouped-centered">
          <button ref='trigger' type='button'>
            Change
          </button>
        </div>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <div class="field is-grouped is-grouped-centered">
          <button class="button is-primary"
                  @click="findCurrencyData">
            Buscar
          </button>
        </div>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <line-chart :chart-data="datacollection" style="width: 700px; height: 700px;"></line-chart>
      </div>
      <div class="column" v-if="currency !== 'TIIE'">
        <table class="table">
          <thead>
            <tr>
              <th>Día</th>
              <th>Valor</th>
            </tr>
          </thead>
          <thead :key="index" v-for="(value, index) in data">
            <tr>
              <td>{{value.fecha}}</td>
              <td>{{value.dato}}</td>
            </tr>
          </thead>
        </table>
      </div>
      <div class="column" v-if="currency !== 'TIIE'">
        <table class="table">
          <thead>
            <tr>
              <th>Valor promedio</th>
              <th>Valor maximo</th>
              <th>Valor minimo</th>
            </tr>
          </thead>
          <thead>
            <tr>
              <td>$ {{promedio}}</td>
              <td>$ {{maximo}}</td>
              <td>$ {{minimo}}</td>
            </tr>
          </thead>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import LineChart from './LineChart.js'
import bulmaCalendar from 'bulma-calendar';

export default {
  components: {
    LineChart
  },
  data () {
    return {
      datacollection: null,
      date: new Date(),
      currency: '',
      init: null,
      end: null,
      maximo: 0,
      minimo: 0,
      promedio: 0,
      data: null,
    }
  },
  mounted () {
    this.fillData();
    const calendar = new bulmaCalendar(this.$refs.trigger, {
      startDate: this.foundation_date,
      type: 'date',
      isRange: true,
    });
    // eslint-disable-next-line no-return-assign
    calendar.on('date:selected', (e) => (this.date = e.start || null));
    calendar.on('select', (e) => {
      const date = e.data.value().split(' - ');
      this.init = this.formatDate(date[0]);
      this.end = this.formatDate(date[1]);
    });
  },
  methods: {
    formatDate(date) {
      const d = new Date(date);
      let month = `${d.getMonth() + 1}`;
      let day = `${d.getDate()}`;
      const year = d.getFullYear();
      // eslint-disable-next-line no-const-assign
      if (month.length < 2) month = `0${month}`;
      if (day.length < 2) day = `0${day}`;
      return [year, month, day].join('-');
    },
    findSerieName(serie) {
      if (serie === 'SF331451') {
        return 'TIIE de fondeo a un día'
      } else if (serie === 'SF43783') {
        return 'TIIE a 28 días'
      } else {
        return 'TIIE a 91 días'
      }
    },
    findCurrencyData(){
      if (this.currency && this.init && this.end) {
        const requestData = {
          currency: this.currency,
          init_date: this.init,
          end_date: this.end,
        }
        this.$store.dispatch('getCurrencyData', requestData)
          .then((res) => {
            if (requestData.currency === 'TIIE') {
              let data = Array();
              let labels = null;
              res.forEach((e) => {
                data.push({
                  label: e.idSerie,
                  data: e.datos.map(a => a.dato)
                })
                if (e.idSerie === 'SF43783') {
                  labels = e.datos.map(a => a.fecha)
                }
              })
              this.datacollection = {
                labels: labels,
                datasets: [
                  {
                    label: this.findSerieName(data[0].label),
                    backgroundColor: '#ffbb33',
                    data: data[0].data
                  },
                  {
                    label: this.findSerieName(data[1].label),
                    backgroundColor: '#a4fe37',
                    data: data[1].data
                  },
                  {
                    label: this.findSerieName(data[2].label),
                    backgroundColor: '#37fecb',
                    data: data[2].data
                  }
                ]
              }
            } else {
              this.data = res.valores;
              this.promedio = res.promedio;
              this.maximo = res.max;
              this.minimo = res.min;
              let labels = new Array();
              let data = new Array();
              res.valores.forEach((e) => {
                labels.push(e.fecha);
                data.push(e.dato)
              })
              this.datacollection = {
                labels: labels,
                datasets: [
                  {
                    label: this.currency,
                    backgroundColor: '#ffbb33',
                    data: data,
                  }
                ]
              }
            }
          })
          .catch((err) => {
            console.log(err);
          })
      } else {
        alert("los cambios de tipo de cambio y las fechas deben ser llenados")
      }
    },
    fillData () {
      this.datacollection = {
        labels: [1,2,3,4,5,6],
      }
    },
    getRandomInt () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    }
  }
}
</script>

<style>
.small {
  max-width: 600px;
  margin:  150px auto;
}
</style>
