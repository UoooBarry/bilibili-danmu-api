<template>
  <v-container>
    <h1>Danmu fetch</h1>
    <v-row>
      <v-col cols="11">
        <v-text-field
          label="Bilibili video"
          v-model="bv"
          @keydown.enter="fetchDanmus()"
        ></v-text-field>
      </v-col>
      <v-col>
        <v-btn color="primary" @click="fetchDanmus()"> Fetch </v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-data-table :headers="headers" :items="danmus" class="elevation-1">
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title> Damus list </v-toolbar-title>
            </v-toolbar>
          </template>
          <template v-slot:[`item.time`]="{ item }">
            {{ secondsToMinute(item.time) }}
          </template>
          <template v-slot:[`item.send_time`]="{ item }">
            {{ timestampToDate(item.send_time) }}
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { getDanmus } from "@/api/danmu";
export default {
  name: "Dashboard",
  data() {
    return {
      bv: "BV1Mq4y137Di",
      danmus: [],
      headers: [
        { text: "UID", value: "crc32_id", sortable: false },
        { text: "Text", value: "text", sortable: false },
        { text: "At (video time)", value: "time" },
        { text: "Send time", value: "send_time" },
      ],
    };
  },
  methods: {
    fetchDanmus() {
      if (!this.bv) return;

      getDanmus(this.bv).then((res) => {
        this.danmus = res.data;
      });
    },
    secondsToMinute(time) {
     const minutes = Math.floor(time / 60);
     const seconds = parseInt(time - minutes * 60); 
     return `${minutes}:${seconds}`
    },
    timestampToDate(time) {
      const date = new Date(time * 1000);
      return this.dateToYMD(date);
    },
    dateToYMD(date) {
      const d = date.getDate();
      const m = date.getMonth() + 1;
      const y = date.getFullYear();
      const hours = date.getHours();
      const minute = date.getMinutes();
      return '' + y + '-' + (m<=9 ? '0' + m : m) + '-' + (d <= 9 ? '0' + d : d) + ' ' + hours + ':' + (minute <= 9 ? '0' + minute : minute);
    }
  },
};
</script>
