import{S as T,i as C,s as H,e as L,h as d,D as f,k as g,F as M,q as c,K as S,N as q,B as z,v,w as h,t as b,b as k,x as w,y as B,z as D,d as j,A,C as E,P as F}from"./index.06513bff.js";function K(n){let e;return{c(){e=L("div"),d(e,"id",n[0]),d(e,"class","prose svelte-86o770"),d(e,"data-testid","markdown"),f(e,"min",n[3]),f(e,"hide",!n[1])},m(s,t){g(s,e,t),e.innerHTML=n[2],n[5](e)},p(s,[t]){t&4&&(e.innerHTML=s[2]),t&1&&d(e,"id",s[0]),t&8&&f(e,"min",s[3]),t&2&&f(e,"hide",!s[1])},i:M,o:M,d(s){s&&c(e),n[5](null)}}}function N(n,e,s){let{elem_id:t=""}=e,{visible:l=!0}=e,{value:u}=e,{min_height:_=!1}=e;const o=S();let i;function r(a){q[a?"unshift":"push"](()=>{i=a,s(4,i)})}return n.$$set=a=>{"elem_id"in a&&s(0,t=a.elem_id),"visible"in a&&s(1,l=a.visible),"value"in a&&s(2,u=a.value),"min_height"in a&&s(3,_=a.min_height)},n.$$.update=()=>{n.$$.dirty&4&&o("change")},[t,l,u,_,i,r]}class P extends T{constructor(e){super(),C(this,e,N,K,H,{elem_id:0,visible:1,value:2,min_height:3})}}function p(n){let e,s,t,l,u;const _=[n[3],{variant:"center"}];let o={};for(let i=0;i<_.length;i+=1)o=B(o,_[i]);return e=new D({props:o}),l=new P({props:{min_height:n[3]&&n[3].status!=="complete",value:n[2],elem_id:n[0],visible:n[1]}}),l.$on("change",n[5]),{c(){v(e.$$.fragment),s=j(),t=L("div"),v(l.$$.fragment),d(t,"class","svelte-1ed2p3z"),f(t,"pending",n[3]?.status==="pending")},m(i,r){h(e,i,r),g(i,s,r),g(i,t,r),h(l,t,null),u=!0},p(i,r){const a=r&8?A(_,[E(i[3]),_[1]]):{};e.$set(a);const m={};r&8&&(m.min_height=i[3]&&i[3].status!=="complete"),r&4&&(m.value=i[2]),r&1&&(m.elem_id=i[0]),r&2&&(m.visible=i[1]),l.$set(m),r&8&&f(t,"pending",i[3]?.status==="pending")},i(i){u||(b(e.$$.fragment,i),b(l.$$.fragment,i),u=!0)},o(i){k(e.$$.fragment,i),k(l.$$.fragment,i),u=!1},d(i){w(e,i),i&&c(s),i&&c(t),w(l)}}}function G(n){let e,s;return e=new z({props:{visible:n[1],elem_id:n[0],disable:!0,$$slots:{default:[p]},$$scope:{ctx:n}}}),{c(){v(e.$$.fragment)},m(t,l){h(e,t,l),s=!0},p(t,[l]){const u={};l&2&&(u.visible=t[1]),l&1&&(u.elem_id=t[0]),l&143&&(u.$$scope={dirty:l,ctx:t}),e.$set(u)},i(t){s||(b(e.$$.fragment,t),s=!0)},o(t){k(e.$$.fragment,t),s=!1},d(t){w(e,t)}}}function I(n,e,s){let{label:t}=e,{elem_id:l=""}=e,{visible:u=!0}=e,{value:_=""}=e,{loading_status:o}=e;const i=S();function r(a){F.call(this,n,a)}return n.$$set=a=>{"label"in a&&s(4,t=a.label),"elem_id"in a&&s(0,l=a.elem_id),"visible"in a&&s(1,u=a.visible),"value"in a&&s(2,_=a.value),"loading_status"in a&&s(3,o=a.loading_status)},n.$$.update=()=>{n.$$.dirty&16&&i("change")},[l,u,_,o,t,r]}class J extends T{constructor(e){super(),C(this,e,I,G,H,{label:4,elem_id:0,visible:1,value:2,loading_status:3})}}var Q=J;const R=["static"],U=n=>({type:"string",description:"HTML rendering of markdown"});export{Q as Component,U as document,R as modes};
//# sourceMappingURL=index.73f4d74b.js.map
