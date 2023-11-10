<template>
    <qrcode-stream @detect="onDetect"></qrcode-stream>
</template>

<script>
import { QrcodeStream } from "vue-qrcode-reader";
import axios from "axios";


export default {
    methods: {
        onDetect (detectedCodes) {
            axios
            .post("/api/v1/reservation/reservation/scan/"+detectedCodes[0].codeResult.code, {
                withCredentials: false, // Ensure credentials are not sent
            })
            .then((response) => {
                data = response.data;
                // check if data has key "message"
                if (data.hasOwnProperty("message")){
                    // scan successful show message
                    this.$q.notify({
                        message: data.message,
                        color: "green",
                        position: "top",
                        icon: "check",
                        timeout: 2000,
                    });
                }else {
                    // scan failed
                    this.$q.notify({
                        message: data.detail,
                        color: "red",
                        position: "top",
                        icon: "warning",
                        timeout: 2000,
                    });
                }
            })
            .catch((error) => {
                // Handle error
                console.log(error);
            });
        }
    }
}