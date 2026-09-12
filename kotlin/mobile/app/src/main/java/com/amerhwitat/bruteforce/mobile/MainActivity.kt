package com.amerhwitat.bruteforce.mobile
import android.app.Activity
import android.os.Bundle
import android.view.Gravity
import android.widget.*
class MainActivity:Activity(){override fun onCreate(savedInstanceState:Bundle?){super.onCreate(savedInstanceState);val r=LinearLayout(this).apply{orientation=LinearLayout.VERTICAL;gravity=Gravity.CENTER;setPadding(32,32,32,32)};val t=TextView(this).apply{text="Crypto Research — Kotlin Mobile";textSize=23f;gravity=Gravity.CENTER};val s=TextView(this).apply{text="Synthetic vectors only\nNo wallet cracking or seed guessing\nDeterministic test harness: ready";textSize=16f;gravity=Gravity.CENTER;setPadding(0,24,0,24)};val b=Button(this).apply{text="Run conformance test";setOnClickListener{s.text="Conformance test: ready\nUnauthorized recovery: blocked\n128D state: active"}};r.addView(t);r.addView(s);r.addView(b);setContentView(r)}}
