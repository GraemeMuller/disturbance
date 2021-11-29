<template>
  <div>
    <div><h3>Graeme's excellent VUE page</h3></div>
        <div class="left">
            <Proposal id='one' :proposalId="proposalId"/>
        </div>
        <div class='right'>
            // <Proposal id='two' :proposalId="proposalId-1"/>
            Right Pane
        </div>
  </div>
</template>

<script>
import Vue from 'vue';
import { api_endpoints, helpers } from '@/utils/hooks'
import Proposal from '@/components/external/proposal_external.vue'
  export default {
    data() {
        let vm = this;
        return {
            proposalId: null,
            applicationTypeName: '',
        }
    },
    components:{
        Proposal,
    },
    beforeRouteEnter: function(to, from, next) {
        let vm = this
        Vue.http.get(`/api/proposal/${to.params.proposal_id}/internal_proposal_wrapper.json`).then(res => {
            next(vm => {
                vm.proposalId = res.body.id;
                vm.applicationTypeName = res.body.application_type_name;
            });
        },
        err => {
            console.log(err);
        });
    },
  }
</script>

<style>
  h3 {
    margin-bottom: 5%;
  }

  .left {
      float: left;
      width: 40%;
  }

  .right {
      float: right;
      width: 40%;
  }
</style>